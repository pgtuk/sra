from sanic import Sanic

import config
from views import sra_bp

app = Sanic(__name__)
app.config.from_object(config)

app.blueprint(sra_bp)

app.run(host=app.config.HOST, port=app.config.PORT)