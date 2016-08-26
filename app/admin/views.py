#!/usr/bin/env python
# -*- coding:utf8 -*-
from flask import url_for,redirect
#from flask_login import current_user
from flask_admin import (Admin,BaseView as _BaseView,AdminIndexView as _AdminIndexView,expose)
from flask_admin.contrib.sqla import ModelView as _ModelView

class AuthMixin(object):
    def is_accessible(self):
        return True 
#        return  current_user.is_authenticated and current_user.username == 'admin'


class AdminIndexView(_AdminIndexView):
    @expose('/')
    def index(self):
        return self.render(self._template)
        #if current_user.is_authenticated and current_user.username=='admin':
        #    return self.render(self._template)
        #else:
        #    return redirect(url_for('/'))

class BaseView(AuthMixin,_BaseView):
    pass

class ModelView(AuthMixin,_ModelView):
    pass


#class UserAdminView(ModelView):
#    column_list = ['username','email','display_name','dynamic','about_me']

