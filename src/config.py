#Dicioario de provedores de email - Facilita a expansão para empresas que utilizam provedores específicos (Ex: Outlook, Yahoo)
SMTP_SETTINGS = {
    "gmail": {
        "host": "smtp.gmail.com",
        "port": 587,
        "use_tls": True
    },
    "outlook": {
        "host": "smtp.office365.com",
        "port": 587,
        "use_tls": True
    },
    "yahoo_jp": {
        "host": "smtp.mail.yahoo.co.jp",
        "port": 465,
        "use_tls": True # Yahoo Japão também exige SSL
    }
}   


# Configuracoes parão do sistema
DEFALT_CHARSET = "utf-8" # Garante suporte a caracteres internacionais (Japonês/Português)
APP_NAME = "MailBot Enterprise"