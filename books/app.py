from flask import Flask, jsonify

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import app_config

db = SQLAlchemy()
ma = Marshmallow()


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

    from .blueprints.books import books as books_blueprint
    app.register_blueprint(books_blueprint)

    # from .blueprints.partner import partner as partner_blueprint
    # app.register_blueprint(partner_blueprint, url_prefix='/partner')

    # from .blueprints.home import home as home_blueprint
    # app.register_blueprint(home_blueprint)

    # from .blueprints.admin import admin as admin_blueprint
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')
    
    return app










