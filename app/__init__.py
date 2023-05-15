from flask import *

from config import Config
from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    
    from app.user import bp as user_bp
    app.register_blueprint(user_bp)

    return app
