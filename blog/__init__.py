from flask import Flask, url_for
from config import inject_context

def create_app():
    app = Flask(__name__)

    # Registrar el context processor
    inject_context(app)

    # Registra las rutas
    from .routes import blog
    app.register_blueprint(blog)

    return app
