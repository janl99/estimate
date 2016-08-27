#!/usr/bin/evn python
# -*- coding:utf8 -*-

from urlparse import urljoin
from datetime import datetime,timedelta
from flask import request,redirect,render_template,url_for,abort,flash,g,session
from flask import current_app,make_response
from sqlalchemy.sql.expression import func
#from flask_login import current_user,login_required
#from accounts.models import User
from main.forms import QueryForm
from main.models import Process,Part
from estimate import db


def get_query_data():
    query_mould_id = 0
    query_material_id = 0
    query_length = 0
    query_width = 0
    query_height = 0
    query_top = 10
    query_parm = {'query_mould_id':query_mould_id,\
            'query_material_id':query_material_id,\
            'query_length':query_length,\
            'query_width':query_width,\
            'query_height':query_height,\
            'query_top':query_top}
    return query_parm

def get_base_data():
    query_parm = get_query_data()
    data = {'query_parm':query_parm,'result_time':0,'result_count':0}

    return data

def query_parts_data(mould_id,material_id,length,width,height):
    if mould_id == 0 and material_id == 0 :
        return Part.query.\
            order_by(func.abs(length - Part.parts_length) + func.abs(width - Part.parts_width) + func.abs(height - Part.parts_height)).\
            limit(10).all()
    elif material_id > 0 and mould_id == 0:
        return Part.query.\
            order_by(func.abs(length - Part.parts_length) + func.abs(width - Part.parts_width) + func.abs(height - Part.parts_height)).\
            filter(Part.material_id == material_id).limit(10).all()
    elif material_id == 0 and mould_id > 0:
        return Part.query.\
            order_by(func.abs(length - Part.parts_length) + func.abs(width - Part.parts_width) + func.abs(height - Part.parts_height)).\
            filter(Part.mould_id == mould_id).limit(10).all()
    elif material_id > 0 and mould_id > 0:
        return Part.query.\
            order_by(func.abs(length - Part.parts_length) + func.abs(width - Part.parts_width) + func.abs(height - Part.parts_height)).\
            filter(Part.mould_id == mould_id,Part.material_id == material_id).limit(10).all()



#@login_required
def index():
    data = get_base_data()
    form = QueryForm()
    if form.validate_on_submit():
        print "-----------------get post query data:---------------------------"
        print form.mould.data
        print form.material.data
        print form.spec.data
        mould_id = 0
        if form.mould.data :
           mould_id = form.mould.data.id 
        material_id = 0 
        if form.material.data:
            material_id = form.material.data.id
        length = 0
        width = 0
        height = 0
        spec = '0x0x0'
        if form.spec.data:
            spec = str(form.spec.data)

        length = spec.split('x')[0]
        width = spec.split('x')[1]
        height = spec.split('x')[2]
        print mould_id
        print material_id
        print length
        print width
        print height

        start_time = datetime.now()
        parts_data = query_parts_data(mould_id,material_id,length,width,height) 
        end_time = datetime.now()
        data["parts"] = parts_data
        data["result_time"] = (end_time - start_time).seconds 
        data["result_count"] = len(parts_data)

    return render_template("main/index.html",form=form,data=data)
