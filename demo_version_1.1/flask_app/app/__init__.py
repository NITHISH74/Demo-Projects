# app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register the custom filter
    app.jinja_env.filters['floatformat'] = floatformat

    # Import and register the blueprint
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

def floatformat(value, precision=2):
    """
    Custom filter to format float numbers to a given precision.
    """
    try:
        return f"{value:.{precision}f}"
    except (ValueError, TypeError):
        return value
