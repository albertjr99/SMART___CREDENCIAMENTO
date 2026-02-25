"""
tcees_client.py – substitui tcees_validator.py no PythonAnywhere.

Drop-in replacement: expõe as mesmas funções (validate_pdf_with_tcees,
validate_multiple_pdfs) com a mesma assinatura e mesmo dict de retorno.

No app.py, basta trocar UMA linha de import:

  ANTES:  from tcees_validator import validate_pdf_with_tcees, validate_multiple_pdfs
  DEPOIS: from tcees_client  import validate_pdf_with_tcees, validate_multiple_pdfs

Variáveis de ambiente necessárias no PythonAnywhere:
  TCEES_SERVICE_URL   → URL do microserviço no Render
                        ex: https://tcees-validator.onrender.com
  TCEES_API_SECRET    → chave gerada pelo Render (copie do painel Environment)
  TCEES_CLIENT_TIMEOUT → segundos de timeout HTTP (padrão: 90)
"""

import os
import logging
from concurrent.futures import ThreadPoolExecutor

import requests

log = logging.getLogger(__name__)

_SERVICE_URL = os.getenv("TCEES_SERVICE_URL", "").rstrip("/")
_API_SECRET  = os.getenv("TCEES_API_SECRET", "")
_TIMEOUT     = int(os.getenv("TCEES_CLIENT_TIMEOUT", "90"))


# ---------------------------------------------------------------------------
# Dict de erro padronizado – mesmo formato que tcees_validator.py retorna
# ---------------------------------------------------------------------------

def _error_result(pdf_path: str, codigo: str, mensagem: str, tecnico: str = "") -> dict:
    """Retorna um dict de erro compatível com o que app.py espera."""
    return {
        "nome_arquivo":       os.path.basename(pdf_path),
        "extensao_valida":    False,
        "sem_senha":          False,
        "tamanho_arquivo_ok": False,
        "tamanho_pagina_ok":  False,
        "assinado":           False,
        "numero_assinaturas": 0,
        "autenticidade_ok":   False,
        "integridade_ok":     False,
        "pesquisavel":        False,
        "resultado_final":    "ERRO",
        "pontuacao":          0,
        "titular_certificado": "",
        "emissor_certificado": "",
        "validade_certificado": "",
        "erro":               mensagem,
        "erro_codigo":        codigo,
        "erro_tecnico":       tecnico,
    }


def _service_ok() -> bool:
    return bool(_SERVICE_URL)


# ---------------------------------------------------------------------------
# Funções públicas (mesma assinatura do tcees_validator.py original)
# ---------------------------------------------------------------------------

def validate_pdf_with_tcees(pdf_path: str) -> dict:
    """
    Envia o PDF ao microserviço TCEES e retorna o dict completo de validação.
    Compatível com a versão local – app.py não precisa mudar nada além do import.
    """
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

    try:
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

        data = resp.json()
        log.info("TCEES service retornou: resultado_final=%s pontuacao=%s",
                 data.get("resultado_final"), data.get("pontuacao"))
        return data

    except requests.exceptions.ConnectionError as exc:
        msg = str(exc)
        log.error("Sem conexão com o microserviço TCEES: %s", msg[:200])
        return _error_result(
            pdf_path,
            "TCEES_SERVICE_UNREACHABLE",
            "Microserviço de validação TCEES temporariamente inacessível.",
            msg[:300],
        )

    except requests.exceptions.Timeout:
        log.error("Timeout ao chamar microserviço TCEES (>%ss).", _TIMEOUT)
        return _error_result(
            pdf_path,
            "TCEES_SERVICE_TIMEOUT",
            f"Microserviço TCEES não respondeu em {_TIMEOUT}s.",
        )

    except Exception as exc:
        log.exception("Erro inesperado ao chamar microserviço TCEES.")
        return _error_result(
            pdf_path,
            "TCEES_CLIENT_ERROR",
            "Erro inesperado ao contatar microserviço de validação.",
            str(exc)[:300],
        )


def validate_multiple_pdfs(pdf_paths: list, max_workers: int = 3) -> list:
    """
    Valida múltiplos PDFs em paralelo via microserviço.
    Mesma assinatura do validate_multiple_pdfs original.
    """
    if not pdf_paths:
        return []

    pdf_paths = pdf_paths[:3]  # limite igual ao original

    print(f"\n[🚀] Iniciando validação paralela de {len(pdf_paths)} documento(s) via microserviço...")

    with ThreadPoolExecutor(max_workers=min(max_workers, len(pdf_paths))) as executor:
        results = list(executor.map(validate_pdf_with_tcees, pdf_paths))

    return results
