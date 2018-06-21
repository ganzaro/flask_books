import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Common configurations
    """

    DEBUG = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEVELOPMENT = True
    DEBUG = True

    SQLALCHEMY_ECHO = False

    # SERVER_NAME = 'localhost:8087'



class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
    # SENDGRID_DEFAULT_FROM = os.environ.get('SENDGRID_DEFAULT_FROM')
    # SECRET_KEY = os.environ.get('SECRET_KEY')

    # SERVER_NAME = '176.58.123.168:5000'


class HerokuConfig(Config):
    # SERVER_NAME = 'blah.herokuapp.com'    
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
    # SENDGRID_DEFAULT_FROM = os.environ.get('SENDGRID_DEFAULT_FROM')
    # SECRET_KEY = os.environ.get('SECRET_KEY')


class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'testing': TestingConfig
}
