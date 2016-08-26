#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
STATIC_FOLDER = os.path.join(BASEDIR,'static')
UPLOAD_FOLDER = os.path.join(STATIC_FOLDER,'uploads')
UPLOAD_AVATAR = os.path.join(UPLOAD_FOLDER,'avatar')

SystemSettings = {
    'pagination':{
        'per_page':int(os.environ.get('per_page',5)),
        'admin_per_page':int(os.environ.get('admin_per_page',10)),
    },
    'copyright':{
        'copyright_msg':os.environ.get('copyright_msg','this is produtc_handover system.').decode('utf8')
    },
}


class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    DATA_DIR = os.path.join(BASE_DIR,'data')
    CSRF_ENABLE = True
    SECRET_KEY = 'you-will-never-guess'

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DATA_DIR,'app.db')

    TEMPLATE_PATH = os.path.join(BASE_DIR,'templates').replace('\\','/')
    STATIC_PATH = os.path.join(BASE_DIR,'static').replace('\\','/')

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True

class PrdConfig(Config):
    DEBUG = os.environ.get('DEBUG','false').lower() == 'true'


config = {
    'dev':DevConfig,
    'prd':PrdConfig,
    'default':DevConfig,
}
