from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import routes at the end to avoid circular imports
    from .routes import main
    app.register_blueprint(main)

    return app
