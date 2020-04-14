"""FlaskのConfigを提供する"""
import os


class ProductionConfig:

    # Flask
    DEBUG = False

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(**{
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'Mitsuya90'),
        'host': os.getenv('DB_HOST', 'chat-mysql-prod'),
        'database': os.getenv('DB_DATABASE', 'prod'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(**{
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'Mitsuya90'),
        'host': os.getenv('DB_HOST', 'chat-mysql-dev'),
        'database': os.getenv('DB_DATABASE', 'dev'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class TestingConfig:

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(**{
        'user': os.getenv('DB_TEST_USER', 'root'),
        'password': os.getenv('DB_TEST_PASSWORD', 'default'),
        'host': os.getenv('DB_TEST_HOST', 'chat-mysql-test'),
        'database': os.getenv('DB_TEST_DATABASE', 'default'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

# Config = DevelopmentConfig
if os.getenv('ENV') == 'production':
    Config = ProductionConfig
elif os.getenv('ENV') == 'development':
    Config = DevelopmentConfig
else:
    Config = TestingConfig
