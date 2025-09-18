import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# # Self-hosted Model Configuration - just uncomment wheneever new environment ready 1 for hosting and other for embedding 
# OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "http://62.169.159.70:8000/v1")
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "not-needed")
# OPENAI_EMBEDDING_BASE = os.getenv("OPENAI_EMBEDDING_BASE", "http://62.169.159.36:8000/v1")
# OPENAI_EMBEDDING_KEY = os.getenv("OPENAI_EMBEDDING_KEY", "dummy")



# Model Configuration
LLM_MODEL = os.getenv("LLM_MODEL", "openai/gpt-oss-20b")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "BAAI/bge-m3")

# Legacy Euri AI Configuration (keeping for backward compatibility)
EURI_API_KEY = os.getenv("EURI_API_KEY", "euri-260e447ef9308db43bf0f5259e1913fdeca5592c058784c3e46bba5d9dd45f39")

# Email Configuration
EMAIL_CONFIG = {
    'smtp_server': os.getenv("EMAIL_SMTP_SERVER", "smtp.gmail.com"),
    'smtp_port': int(os.getenv("EMAIL_SMTP_PORT", "587")),
    'sender_email': os.getenv("EMAIL_SENDER", "your_email@gmail.com"),
    'sender_password': os.getenv("EMAIL_PASSWORD", "your_app_password"),
    'receiver_email': os.getenv("EMAIL_RECEIVER", "sudhanshu@euron.one")
}