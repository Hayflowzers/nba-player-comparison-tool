import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Set the secret key to a random string. Keep this really secret!
    app.secret_key = os.getenv('SECRET_KEY', os.urandom(24))

    # Import routes at the end to avoid circular imports
    from .routes import main
    app.register_blueprint(main)

    return app
