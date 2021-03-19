from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from google.auth import default


# Create credentials
CREDENTIALS, PROJECT = default()

# The storage api scopes and auth url
SCOPES = [
  "https://www.googleapis.com/auth/devstorage.read_only",
  "https://www.googleapis.com/auth/cloud-platform.read-only",
  "https://www.googleapis.com/auth/devstorage.full_control",
  "https://www.googleapis.com/auth/cloud-platform",
  "https://www.googleapis.com/auth/devstorage.read_write"
]
AUTH_URL = f'https://storage.googleapis.com/storage/v1/b/{PROJECT}/o'