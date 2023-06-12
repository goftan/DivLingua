from pathlib import Path

from flask import Flask

from routes import quiz_bp

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / 'frontend'
STATIC_DIR = FRONTEND_DIR / 'static'
TEMPLATES_DIR = FRONTEND_DIR / 'templates'


def create_app():
    app = Flask(__name__,
                static_folder=str(STATIC_DIR),
                template_folder=str(TEMPLATES_DIR))
    app.register_blueprint(quiz_bp, url_prefix='/')
    app.secret_key = "secret key"
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
