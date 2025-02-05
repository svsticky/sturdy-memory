import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# OpenID Connect (OIDC) configuration
OIDC_AUTHORIZATION_URL = os.getenv("OIDC_OP_AUTHORIZATION_URL")
OIDC_TOKEN_URL = os.getenv("OIDC_OP_TOKEN_URL")
OIDC_USERINFO_URL = os.getenv("OIDC_USERINFO_URL")
OIDC_CLIENT_ID = os.getenv("OIDC_CLIENT_ID")
OIDC_CLIENT_SECRET = os.getenv("OIDC_CLIENT_SECRET")
OIDC_REDIRECT_URI = os.getenv("OIDC_REDIRECT_URI")

# PostgreSQL database configuration
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_DSN = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}"

# API metadata for OpenAPI documentation
tags_metadata = [
    # TODO: Add useful metadata for API endpoints after they have been created.
]
