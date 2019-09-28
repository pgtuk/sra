from oauthlib.oauth2.rfc6749.errors import OAuth2Error
from requests_oauthlib import OAuth2Session
from sanic import response, Blueprint
from sanic.exceptions import NotFound

import config

sra_bp = Blueprint('sra')


def _make_session():
    return OAuth2Session(config.GIT_CLIENT_ID, scope='public_repo')


@sra_bp.route('/')
async def auth(request):
    session = _make_session()
    auth_url, _ = session.authorization_url(config.GIT_AUTH_URL)

    return response.redirect(auth_url)


@sra_bp.route('/callback/github')
async def callback_git(request):
    return response.redirect(f'/replicate?{request.query_string}')


@sra_bp.route('/replicate')
async def replicate(request):
    session = _make_session()
    try:
        session.token = session.fetch_token(
            config.GIT_TOKEN_URL, 
            client_secret=config.GIT_CLIENT_SECRET, 
            authorization_response=request.url,
        )
    except OAuth2Error as e:
        return response.text(f'Unaible to fetch github token. Reason: {e.description or "Unknown"}')

    fork_request = session.post(
        f'{config.GIT_API_URL}/repos/{config.GIT_OWNER}/{config.GIT_REPO}/forks'
    )

    if not fork_request.ok:
        return response.text('Fail. No access to self-replicating app repository')

    return response.html(
        'Success. Self-replicating app replicated itself and is available now in ' \
        f'<a href="https://github.com/{fork_request.json()["full_name"]}">your GitHub profile</a>',
    )


@sra_bp.exception(NotFound)
async def handel_404(request, exception):
    return response.text('Oops')