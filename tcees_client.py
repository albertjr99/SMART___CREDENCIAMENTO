"""
tcees_client.py – substitui tcees_validator.py no app.py.

Drop-in replacement: expõe as mesmas funções (validate_pdf_with_tcees,
validate_multiple_pdfs) com a mesma assinatura e mesmo dict de retorno.

No app.py, troque UMA linha:
  ANTES:  from tcees_validator import validate_pdf_with_tcees, validate_multiple_pdfs
  DEPOIS: from tcees_client  import validate_pdf_with_tcees, validate_multiple_pdfs

Variáveis de ambiente necessárias:
  TCEES_SERVICE_URL    → URL do microserviço no Render
  TCEES_API_SECRET     → chave de autenticação
  TCEES_CLIENT_TIMEOUT → timeout em segundos (padrão: 90)
"""

import os
import logging
import time
from concurrent.futures import ThreadPoolExecutor

import requests

log = logging.getLogger(__name__)

_SERVICE_URL = os.getenv("TCEES_SERVICE_URL", "").rstrip("/")
_API_SECRET  = os.getenv("TCEES_API_SECRET", "")
_TIMEOUT     = int(os.getenv("TCEES_CLIENT_TIMEOUT", "90"))
_MAX_RETRIES = 3        # tenta até 3x (cobre o "wake up" do Render free tier)
_RETRY_WAIT  = 10       # segundos entre tentativas


def _error_result(pdf_path: str, codigo: str, mensagem: str, tecnico: str = "") -> dict:
    return {
        "nome_arquivo":        os.path.basename(pdf_path),
        "extensao_valida":     False,
        "sem_senha":           False,
        "tamanho_arquivo_ok":  False,
        "tamanho_pagina_ok":   False,
        "assinado":            False,
        "numero_assinaturas":  0,
        "autenticidade_ok":    False,
        "integridade_ok":      False,
        "pesquisavel":         False,
        "resultado_final":     "ERRO",
        "pontuacao":           0,
        "titular_certificado": "",
        "emissor_certificado": "",
        "validade_certificado": "",
        "erro":                mensagem,
        "erro_codigo":         codigo,
        "erro_tecnico":        tecnico,
    }


def _service_ok() -> bool:
    return bool(_SERVICE_URL)


def _wake_up_service():
    """Faz um ping no /health para acordar o serviço antes de enviar o PDF."""
    try:
        requests.get(f"{_SERVICE_URL}/health", timeout=15)
        time.sleep(3)
    except Exception:
        pass


def validate_pdf_with_tcees(pdf_path: str) -> dict:
    if not _service_ok():
        log.warning("TCEES_SERVICE_URL não configurada.")
        return _error_result(
            pdf_path,
            "TCEES_SERVICE_NOT_CONFIGURED",
            "Serviço de validação TCEES não configurado (TCEES_SERVICE_URL ausente).",
        )

    headers = {}
    if _API_SECRET:
        headers["X-API-Secret"] = _API_SECRET

    # Acorda o serviço antes de enviar o PDF
    _wake_up_service()

    last_error = None
    for attempt in range(1, _MAX_RETRIES + 1):
        try:
            log.info("TCEES validate tentativa %d/%d", attempt, _MAX_RETRIES)
            with open(pdf_path, "rb") as f:
                resp = requests.post(
                    f"{_SERVICE_URL}/validate",
                    files={"file": (os.path.basename(pdf_path), f, "application/pdf")},
                    headers=headers,
                    timeout=_TIMEOUT,
                )

            if resp.status_code == 401:
                return _error_result(
                    pdf_path,
                    "TCEES_AUTH_ERROR",
                    "Erro de autenticação no microserviço TCEES. Verifique TCEES_API_SECRET.",
                )

            # Resposta vazia = serviço ainda acordando, tenta novamente
            if not resp.text or not resp.text.strip():
                log.warning("Resposta vazia do microserviço (tentativa %d) — aguardando...", attempt)
                time.sleep(_RETRY_WAIT)
                continue

            # Resposta não-JSON (ex: página HTML de erro do Render)
            try:
                data = resp.json()
            except Exception:
                log.warning("Resposta não-JSON (tentativa %d): %s", attempt, resp.text[:200])
                time.sleep(_RETRY_WAIT)
                continue

            log.info("TCEES retornou: resultado_final=%s pontuacao=%s",
                     data.get("resultado_final"), data.get("pontuacao"))
            return data

        except requests.exceptions.ConnectionError as exc:
            last_error = str(exc)
            log.error("Sem conexão com microserviço TCEES (tentativa %d): %s", attempt, last_error[:200])
            time.sleep(_RETRY_WAIT)

        except requests.exceptions.Timeout:
            last_error = f"Timeout após {_TIMEOUT}s"
            log.error("Timeout TCEES (tentativa %d)", attempt)
            time.sleep(_RETRY_WAIT)

        except Exception as exc:
            last_error = str(exc)
            log.exception("Erro inesperado TCEES (tentativa %d)", attempt)
            time.sleep(_RETRY_WAIT)

    # Todas as tentativas falharam
    return _error_result(
        pdf_path,
        "TCEES_SERVICE_UNREACHABLE",
        "Serviço de validação TCEES inacessível após múltiplas tentativas.",
        last_error or "",
    )


def validate_multiple_pdfs(pdf_paths: list, max_workers: int = 3) -> list:
    if not pdf_paths:
        return []

    pdf_paths = pdf_paths[:3]
    print(f"\n[🚀] Validando {len(pdf_paths)} documento(s) via microserviço...")

    with ThreadPoolExecutor(max_workers=min(max_workers, len(pdf_paths))) as executor:
        results = list(executor.map(validate_pdf_with_tcees, pdf_paths))

    return results
