import os

from dotenv import load_dotenv
load_dotenv()

HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 5000))


GIT_API_URL = 'https://api.github.com'
GIT_AUTH_URL = 'https://github.com/login/oauth/authorize'
GIT_TOKEN_URL = 'https://github.com/login/oauth/access_token'

GIT_CLIENT_ID = os.getenv('GIT_CLIENT_ID')
GIT_CLIENT_SECRET = os.getenv('GIT_CLIENT_SECRET')

GIT_OWNER = os.getenv('GIT_OWNER', 'pgtuk')
GIT_REPO = os.getenv('GIT_REPO', 'sra')



