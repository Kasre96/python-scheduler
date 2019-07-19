import os


# Development configuration
class DevelopmentConfig:
    SECRET_KEY = 'somerandomnstring'
    FLASK_ENV = os.environ.get('FLASK_ENV') or 'development'
    DEBUG = True

