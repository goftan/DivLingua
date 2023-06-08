# file: main.py

from flask import Flask
from routes import quiz_bp
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / 'frontend'
STATIC_DIR = FRONTEND_DIR / 'static'
TEMPLATES_DIR = FRONTEND_DIR / 'templates'

app = Flask(__name__,
            static_folder=str(STATIC_DIR),
            template_folder=str(TEMPLATES_DIR))

app.register_blueprint(quiz_bp)

if __name__ == '__main__':
    app.run(debug=True)
