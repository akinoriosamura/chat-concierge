"""FlaskのConfigを提供する"""
import os


class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(**{
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'Mitsuya90'),
        'host': os.getenv('DB_HOST', 'chat-mysql'),
        'database': os.getenv('DB_DATABASE', 'chat'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class TestingConfig:

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(**{
        'user': os.getenv('DB_TEST_USER', 'root'),
        'password': os.getenv('DB_TEST_PASSWORD', 'default'),
        'host': os.getenv('DB_TEST_HOST', 'chat-mysql'),
        'database': os.getenv('DB_TEST_DATABASE', 'default'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
