import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env (Segurança acima de tudo)
load_dotenv()

def send_email_pro(receiver_email, subject, body):
    """
    Envia e-mails com suporte a caracteres internacionais (Japonês/Português).
    """
    # Configurações vindas do .env
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Criando a estrutura da mensagem (Padrão MIME para aceitar Japonês)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Garante que o corpo do texto use UTF-8 para não quebrar caracteres japoneses
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        # Envia o e-mail codificado corretamente
        server.send_message(msg)
        print("✅ Success: Email sent to " + receiver_email)
        
    except Exception as e:
        print(f"❌ Error: Failed to send email. \nDetails: {e}")
    finally:
        server.quit()

# Exemplo de uso flexível (Pode ser importado por outros scripts)
if __name__ == "__main__":
    # Testando com Japonês
    destinatario = "exemplo@dominio.com"
    assunto = "Sistema de Notificação - Teste 🇯🇵"
    mensagem = "こんにちは! Este é um teste do MailBot moderno."
    
    send_email_pro(destinatario, assunto, mensagem)