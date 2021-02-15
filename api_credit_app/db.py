import os

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'credit_db',
        'USER': 'postgres',
        'PASSWORD': 'iseedeadpeople',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}