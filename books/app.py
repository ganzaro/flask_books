from flask import Flask, jsonify

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from config import app_config

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
cors = CORS()

def create_app(config_name='development'):
    if config_name == 'heroku':
        app = Flask(__name__)
        app.config.from_object(app_config[config_name])

    else: 
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py')
    
    
    db.init_app(app)
    migrate = Migrate(app, db)

    ma.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)

    from .blueprints.books import books as books_blueprint
    app.register_blueprint(books_blueprint)

    # from .blueprints.boo import boo as boo_bp
    # app.register_blueprint(boo_bp)

    from .blueprints.profile import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)

    from .blueprints.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    #  app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # from .blueprints.admin import admin as admin_blueprint
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')
    
    return app










