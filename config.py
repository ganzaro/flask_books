import os


class Config(object):
    """
    Common configurations
    """

    DEBUG = False
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BCRYPT_LOG_ROUNDS = 13

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # APP_DIR = os.path.abspath(os.path.dirname(__file__))
    # PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))



class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEVELOPMENT = True
    DEBUG = True

    SQLALCHEMY_ECHO = False

    DB_NAME = 'dev.db'

    DB_PATH = os.path.join(Config.BASE_DIR, DB_NAME)

    # DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)

    CELERY_BROKER_URL='redis://localhost:6379'
    CELERY_RESULT_BACKEND='redis://localhost:6379'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_REDIS_MAX_CONNECTIONS = 5

    SERVER_NAME = 'localhost:5002'


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
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    BCRYPT_LOG_ROUNDS = 4


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'testing': TestingConfig
}
