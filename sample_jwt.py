import common
from google.auth.transport.requests import AuthorizedSession

# Create credentials with default scopes so self signed jwt flow is used
credentials = common.CREDENTIALS.with_scopes(None, default_scopes=common.SCOPES)

# Make request, set default_host to trigger self signed jwt
authed_session = AuthorizedSession(credentials, default_host='storage.googleapis.com')
response = authed_session.request('GET', common.AUTH_URL)
print(response.text)