import os

class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY='bdd03968570cdc222dc17123ee8e9f6a',
    PROPAGATE_EXCEPTIONS = True,
    TEMPLATES_AUTO_RELOAD = True,
    # SQLALCHEMY_TRACK_MODIFICATIONS = False,

class ProductionConfig(Config):
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    # SQLALCHEMY_DATABASE_URI = database_url
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
