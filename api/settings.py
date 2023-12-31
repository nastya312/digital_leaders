import os
from pydantic_settings import BaseSettings


class ApiSettings(BaseSettings):
    TITLE: str = 'Api Service for employees'
    DESCRIPTION: str = '''Automatic task distribution service for bank field employees'''
    VERSION: str = '0.0'

    URL: str = os.environ.get('URL', '')
    DEBUG: bool = os.environ.get('DEBUG', True)

    DATETIME_FORMAT: str = os.environ.get('DATETIME_FORMAT', '%Y-%m-%dT%H:%M:%S.%f%z')
    TIME_ZONE: str = 'UTC'

    ORIGINS: list = ['*', 'http:/localhost']
    ALLOW_CREDENTIALS: bool = True
    ALLOW_METHODS: list = ['*']
    ALLOW_HEADERS: list = ['*']

    STATIC_FILES: str = os.environ.get('STATIC_FILES', '/code/static')

    POSTGRES_CONNECT: str = os.environ['POSTGRES_CONNECT']
    POOL: int = os.environ.get('POOL', 50)
    MAX_OVER: int = os.environ.get('MAX_OVER', 100)

    CELERY_BROKER_URL: str = os.environ['CELERY_BROKER_URL']
    CELERY_RESULT_BACKEND: str = os.environ['CELERY_RESULT_BACKEND']

    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES:', 60*60*24*31))
    ALGORITHM: str = os.environ.get('ALGORITHM', '"HS256"')
    SECURITY_KEY: str = os.environ['SECURITY_KEY']

    class Config:
        case_sensitive = True


api_settings = ApiSettings()
