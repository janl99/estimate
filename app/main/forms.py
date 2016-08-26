#!/usr/bin/env python
# -*- coding:utf8 -*-

from flask_wtf import Form
from wtforms import StringField,TextAreaField,DecimalField, BooleanField,SelectField,ValidationError
from wtforms.validators import Required,Length,Email,Regexp,EqualTo,URL,Optional
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import Mould,Material,Part 




def all_moulds():
    mould_data = Mould.query.all()
    return mould_data 


def all_materials():
    material_data = Material.query.all()
    return material_data 

class QueryForm(Form):
    mould = QuerySelectField('Mould',query_factory=all_moulds,allow_blank=True,blank_text="Select Mould")
    material = QuerySelectField('Material',query_factory=all_materials,allow_blank=True,blank_text="Select Material")
    spec = StringField('Spec',[Length(min=5,max=64)]) 


