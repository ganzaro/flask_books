from flask import Flask, jsonify

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import app_config

db = SQLAlchemy()


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

    @app.route('/help', methods = ['GET'])
    def help():
        """Print available functions."""
        func_list = {}
        for rule in app.url_map.iter_rules():
            if rule.endpoint != 'static':
                func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
        return jsonify(func_list)

    from . import models

    # from .blueprints.admin import admin as admin_blueprint
    # app.register_blueprint(admin_blueprint, url_prefix='/admin')

    # from .blueprints.user import user as user_blueprint
    # app.register_blueprint(user_blueprint)

    # from .blueprints.partner import partner as partner_blueprint
    # app.register_blueprint(partner_blueprint, url_prefix='/partner')

    # from .blueprints.home import home as home_blueprint
    # app.register_blueprint(home_blueprint)

    return app

from . import controllers








