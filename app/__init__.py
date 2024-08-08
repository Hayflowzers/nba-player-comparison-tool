from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Optional: Configure app directly if no config.py is used
    #app.config['SECRET_KEY'] = 'your_secret_key_here'
    #app.config['DEBUG'] = True
    
    # Register blueprints, routes, etc.
    from .routes import main
    app.register_blueprint(main)
    
    return app
