import common
from google.auth.transport.requests import AuthorizedSession

# Create credentials with scopes so refresh token flow is used
credentials = common.CREDENTIALS.with_scopes(common.SCOPES)

# Make request
authed_session = AuthorizedSession(credentials)
response = authed_session.request('GET', common.AUTH_URL)
print(response.text)