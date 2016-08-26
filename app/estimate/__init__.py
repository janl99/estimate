import os
from flask import Flask,g
#from flask_login import LoginManager,current_user
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy() 
bootstrap = Bootstrap()
#login_manager = LoginManager()
#login_manager.session_protection = 'strong'
#login_manager.login_view = 'accounts.login'

def create_app(config_name):
    app = Flask(__name__,
        template_folder=config[config_name].TEMPLATE_PATH,static_folder=config[config_name].STATIC_PATH)
    app.config.from_object(config[config_name])

    print "Config_Name:" + config_name
    print "DATA_DIR:" + str(config[config_name].DATA_DIR)
    config[config_name].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
#    login_manager.init_app(app)

    from main.urls import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

# instance app
app = create_app(os.getenv('config') or 'default')

# setup admin
from admin import admin
admin.init_app(app)

#@app.before_request
#def before_request():
#    g.user = current_user
