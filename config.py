from flask import url_for

# Variables de configuración
BLOG_TITLE = "My Flask Blog"
BLOG_AUTHOR = "Marco Antonio Romero"
BLOG_EMAIL = "marcoromero.dev@gmail.com"
BLOG_VERSION = "1.0.0"
BASE_URL = "/"
STATIC_BASE = "assets"
IMG_BASE = "assets/imgs"

def inject_context(app):
    """Registra un context processor en la aplicación Flask."""
    @app.context_processor
    def inject_globals():
        return dict(
            blog_title = BLOG_TITLE,
            blog_author = BLOG_AUTHOR,
            blog_email = BLOG_EMAIL,
            blog_version = BLOG_VERSION,
            base_url = BASE_URL,
            static_base=url_for('static', filename=STATIC_BASE),
            )