"""
Servico de envio de e-mails automaticos.
Suporta SendGrid (API HTTP) e modo de desenvolvimento.
"""

import os
import sqlite3
import requests


class EmailService:
    """Servico de envio de e-mails automaticos."""

    def __init__(self):
        self.email_from = os.getenv('EMAIL_FROM', 'sistema@credenciamento.gov.br')
        self.enabled = os.getenv('EMAIL_ENABLED', 'false').lower() == 'true'
        self.sendgrid_api_key = os.getenv('SENDGRID_API_KEY', '').strip()
        self.app_base_url = os.getenv('APP_BASE_URL', 'http://127.0.0.1:5000').rstrip('/')

    def send_email(self, to_email, to_name, subject, body_html):
        """Envia e-mail para um destinatario."""
        if not to_email:
            return {'success': False, 'error': 'Destinatario sem e-mail cadastrado'}

        if not self.enabled:
            print('Email desabilitado (modo desenvolvimento)')
            print(f'Para: {to_email}')
            print(f'Assunto: {subject}')
            return {'success': True, 'mode': 'development'}

        if not self.sendgrid_api_key:
            error = 'SENDGRID_API_KEY nao configurada'
            print(f'Erro ao enviar e-mail: {error}')
            return {'success': False, 'error': error}

        return self._send_via_sendgrid(to_email, to_name, subject, body_html)

    def _send_via_sendgrid(self, to_email, to_name, subject, body_html):
        payload = {
            'personalizations': [{
                'to': [{'email': to_email, 'name': to_name or ''}],
                'subject': subject
            }],
            'from': {'email': self.email_from, 'name': 'Sistema de Credenciamento'},
            'content': [{
                'type': 'text/html',
                'value': body_html
            }]
        }

        headers = {
            'Authorization': f'Bearer {self.sendgrid_api_key}',
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post(
                'https://api.sendgrid.com/v3/mail/send',
                headers=headers,
                json=payload,
                timeout=20
            )
            if response.status_code in (200, 202):
                print(f'Email enviado para: {to_email}')
                return {'success': True, 'mode': 'sendgrid'}

            error = f'Status {response.status_code}: {response.text[:300]}'
            print(f'Erro ao enviar e-mail (SendGrid): {error}')
            return {'success': False, 'error': error}
        except Exception as e:
            print(f'Erro ao enviar e-mail (SendGrid): {e}')
            return {'success': False, 'error': str(e)}

    def log_email(self, process_id, recipient_email, recipient_name, subject, body, status='sent', error=None):
        """Registra e-mail no banco de dados."""
        try:
            conn = sqlite3.connect('credenciamento.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS email_logs (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            process_id INTEGER,
                            recipient_email TEXT,
                            recipient_name TEXT,
                            subject TEXT,
                            body TEXT,
                            status TEXT,
                            error_message TEXT,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )''')
            c.execute('''INSERT INTO email_logs
                         (process_id, recipient_email, recipient_name, subject, body, status, error_message)
                         VALUES (?, ?, ?, ?, ?, ?, ?)''',
                      (process_id, recipient_email, recipient_name, subject, body, status, error))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f'Erro ao logar e-mail: {e}')

    def _email_wrapper(self, process_id, to_email, to_name, subject, body):
        result = self.send_email(to_email, to_name, subject, body)
        self.log_email(
            process_id=process_id,
            recipient_email=to_email,
            recipient_name=to_name,
            subject=subject,
            body=body,
            status='sent' if result.get('success') else 'failed',
            error=result.get('error')
        )
        return result

    def notify_document_submission(self, process_id, institution_name, rpps_email, rpps_name):
        """IF enviou processo para analise: notificar RPPS."""
        subject = f'Novo processo recebido para analise - {institution_name}'
        body = f"""
        <html><body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2>Sistema de Credenciamento RPPS</h2>
            <p>Ola, <strong>{rpps_name}</strong>,</p>
            <p>A instituicao financeira <strong>{institution_name}</strong> enviou o processo <strong>{process_id}</strong> para analise.</p>
            <p>Acesse o sistema para revisar os documentos.</p>
            <p><a href="{self.app_base_url}/rpps/process/{process_id}">Abrir processo</a></p>
        </body></html>
        """
        return self._email_wrapper(process_id, rpps_email, rpps_name, subject, body)

    def notify_process_returned(self, process_id, institution_email, institution_name, rpps_name, reason, observations=''):
        """RPPS devolveu processo: notificar IF."""
        subject = f'Processo devolvido para correcao - {process_id}'
        body = f"""
        <html><body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2>Sistema de Credenciamento RPPS</h2>
            <p>Ola, <strong>{institution_name}</strong>,</p>
            <p>O RPPS devolveu o processo <strong>{process_id}</strong> para correcao.</p>
            <p><strong>Motivo:</strong> {reason or 'Nao informado'}</p>
            <p><strong>Observacoes:</strong> {observations or 'Sem observacoes adicionais'}</p>
            <p>Entre no sistema para ver os detalhes e reenviar.</p>
            <p><a href="{self.app_base_url}/financial/process/{process_id}">Abrir processo</a></p>
        </body></html>
        """
        return self._email_wrapper(process_id, institution_email, institution_name, subject, body)

    def notify_document_request(self, process_id, institution_email, institution_name, rpps_name, description):
        """RPPS solicitou documento adicional: notificar IF."""
        subject = f'Documento adicional solicitado - {process_id}'
        body = f"""
        <html><body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2>Sistema de Credenciamento RPPS</h2>
            <p>Ola, <strong>{institution_name}</strong>,</p>
            <p>O RPPS solicitou documento adicional no processo <strong>{process_id}</strong>.</p>
            <p><strong>Solicitacao:</strong> {description}</p>
            <p>Entre no sistema para anexar o documento solicitado.</p>
            <p><a href="{self.app_base_url}/financial/process/{process_id}">Abrir processo</a></p>
        </body></html>
        """
        return self._email_wrapper(process_id, institution_email, institution_name, subject, body)

    def notify_process_approved(self, process_id, institution_email, institution_name, rpps_name):
        """RPPS aprovou processo: notificar IF."""
        subject = f'Processo aprovado - {process_id}'
        body = f"""
        <html><body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2>Sistema de Credenciamento RPPS</h2>
            <p>Ola, <strong>{institution_name}</strong>,</p>
            <p>O processo <strong>{process_id}</strong> foi <strong>APROVADO</strong> pelo RPPS.</p>
            <p>Entre no sistema para visualizar o parecer final.</p>
            <p><a href="{self.app_base_url}/financial/process/{process_id}">Abrir processo</a></p>
        </body></html>
        """
        return self._email_wrapper(process_id, institution_email, institution_name, subject, body)

    def notify_process_rejected(self, process_id, institution_email, institution_name, rpps_name, note=''):
        """RPPS rejeitou processo: notificar IF."""
        subject = f'Processo rejeitado - {process_id}'
        body = f"""
        <html><body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2>Sistema de Credenciamento RPPS</h2>
            <p>Ola, <strong>{institution_name}</strong>,</p>
            <p>O processo <strong>{process_id}</strong> foi <strong>REJEITADO</strong> pelo RPPS.</p>
            <p><strong>Observacao:</strong> {note or 'Consulte o sistema para detalhes'}</p>
            <p>Entre no sistema para visualizar o parecer final.</p>
            <p><a href="{self.app_base_url}/financial/process/{process_id}">Abrir processo</a></p>
        </body></html>
        """
        return self._email_wrapper(process_id, institution_email, institution_name, subject, body)

    def notify_credentialing_expiring(self, process_id, rpps_email, rpps_name, institution_name, end_date, days_remaining, is_legacy=False):
        """Notifica RPPS que um credenciamento aprovado está próximo do vencimento."""
        origem = 'Credenciamento legado' if is_legacy else 'Credenciamento'
        subject = f'Vencimento próximo ({days_remaining} dias) - {process_id}'
        body = f"""
        <html><body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2>Sistema de Credenciamento RPPS</h2>
            <p>Olá, <strong>{rpps_name}</strong>,</p>
            <p><strong>{origem}</strong> vinculado à instituição <strong>{institution_name}</strong> está próximo do vencimento.</p>
            <p><strong>Identificação:</strong> {process_id}</p>
            <p><strong>Validade final:</strong> {end_date}</p>
            <p><strong>Dias restantes:</strong> {days_remaining}</p>
            <p>Recomendamos iniciar o processo de renovação antes da data limite.</p>
            <p><a href="{self.app_base_url}/rpps/home">Abrir painel RPPS</a></p>
        </body></html>
        """
        return self._email_wrapper(process_id, rpps_email, rpps_name, subject, body)


email_service = EmailService()
