
import smtplib
import uuid
import qrcode
import os
from email.message import EmailMessage

# Configuração do servidor de e-mail (exemplo com Gmail)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "seuemail@gmail.com"
EMAIL_PASSWORD = "suasenha"


def gerar_ingresso(self, cinema, filme, cadeiras):
    email = self.user.email

    # Criar um código único para o ingresso
    codigo_ingresso = str(uuid.uuid4())[:8]

    # Criar os detalhes do ingresso como string
    detalhes_ingresso = f"ID: {codigo_ingresso}\nCinema: {cinema}\nFilme: {filme}\nCadeiras: {', '.join(cadeiras)}"

    # Gerar QR Code
    qr = qrcode.make(detalhes_ingresso)

    # Criar diretório para salvar ingressos (se não existir)
    os.makedirs("ingressos", exist_ok=True)

    # Caminho do QR Code
    qr_path = f"ingressos/{codigo_ingresso}.png"
    qr.save(qr_path)

    # Criar ingresso com ID e QR Code
    ingresso = {
        "id": codigo_ingresso,
        "Cinema": cinema,
        "Filme": filme,
        "Cadeiras": cadeiras,
        "QR Code": qr_path  # Caminho da imagem do QR Code
    }

    # Adicionar ao histórico do usuário
    self.users[email]["history"].append(ingresso)
    self.save_users()

    # Enviar e-mail com QR Code
    self.enviar_email_ingresso(email, detalhes_ingresso, qr_path)

    print(f"Ingresso gerado e enviado para {email}! Código: {codigo_ingresso}")
    return ingresso

def enviar_email_ingresso(self, destinatario, detalhes, qr_path):
    # Criar e-mail
    msg = EmailMessage()
    msg["Subject"] = "Seu ingresso de cinema"
    msg["From"] = EMAIL_SENDER
    msg["To"] = destinatario
    msg.set_content(f"Olá!\n\nAqui está o seu ingresso:\n\n{detalhes}\n\nApresente o QR Code na entrada do cinema.")

    # Anexar QR Code ao e-mail
    with open(qr_path, "rb") as f:
        img_data = f.read()
        msg.add_attachment(img_data, maintype="image", subtype="png", filename="Ingresso_QR.png")

    # Enviar e-mail via servidor SMTP
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Segurança
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print("Erro ao enviar e-mail:", e)
