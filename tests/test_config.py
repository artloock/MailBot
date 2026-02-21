import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config import SMTP_SETTINGS

def test_environment():
    print("🔍 Verificando ambiente...")

    # Teste 1: Verifica se o .env foi criado (indiretamente via variável)
    from dotenv import load_dotenv
    load_dotenv()
    if os.getenv("EMAIL_USER"):
        print("✅ Variáveis de ambiente: OK")
    else:
        print("❌ Erro: EMAIL_USER não encontrado no .env")

    # Teste 2: Verifica se as configurações de SMTP estão carregando
    if "gmail" in SMTP_SETTINGS:
        print("✅ Configurações de SMTP: OK")
    else:
        print("❌ Erro: SMTP_SETTINGS não carregado corretamente")

if __name__ == "__main__":
    test_environment()