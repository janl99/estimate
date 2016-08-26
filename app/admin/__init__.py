#!/usr/bin/env python
# -*- coding:utf8 -*-

from flask_admin import Admin
from estimate import db
from views import ModelView
#from accounts.models import User
from main.models import Material,Mould,Part,Process 

admin = Admin(name="Estimate.Admin")

#admin.add_view(UserAdminView(User,db.session))
admin.add_view(ModelView(Material,db.session))
admin.add_view(ModelView(Mould,db.session))
admin.add_view(ModelView(Part,db.session))
admin.add_view(ModelView(Process,db.session))

