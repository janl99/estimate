#!/usr/bin/env python
# -*- coding:utf8 -*-

from estimate import db
from decimal import *

class Material(db.Model):
    __tablename__ = "materials"
    id = db.Column(db.Integer,primary_key = True)
    material_name = db.Column(db.String(64))
    parts = db.relationship('Part',backref='material')

    def __unicode__(self):
        return self.material_name

    def __repr__(self):
        return '<Material %r>' % self.material_name

class Mould(db.Model):
    __tablename__ = "moulds"
    id = db.Column(db.Integer,primary_key = True)
    mould_name = db.Column(db.String(64)) 
    mould_code = db.Column(db.String(16))
    parts = db.relationship('Part',backref='mould')

    def __unicode__(self):
        return self.mould_name + "-" +  self.mould_code 

    def __repr__(self):
        return '<Mould %r:%r>' % (self.mould_name,self.mould_code)

class Part(db.Model):
    __tablename__ = "parts"
    id = db.Column(db.Integer,primary_key = True)
    mould_id = db.Column(db.Integer,db.ForeignKey("moulds.id")) 
    parts_name = db.Column(db.String(64))
    material_id = db.Column(db.Integer,db.ForeignKey("materials.id"))
    quantity = db.Column(db.Integer)
    parts_length =db.Column(db.Integer)
    parts_width = db.Column(db.Integer)
    parts_height = db.Column(db.Integer) 
    note = db.Column(db.String(128))
    processes = db.relationship('Process',backref='part',lazy='immediate')

    def __unicode__(self):
        return self.parts_name + ":" + str(self.parts_length) + "x" + str(self.parts_width) + "x" + str(self.parts_height)

    def __repr__(self):
        return '<Part %r:%dx%dx%d>' % (self.parts_name,self.parts_length,self.parts_width,self.parts_height)

    @property 
    def working_hours(self):
        hours = Decimal(0.00)
        for p in self.processes:
            print p.working_hours
            hours = hours + p.working_hours
            print hours
        return hours   



class Process(db.Model):
    __tablename__ = "processes"
    id = db.Column(db.Integer,primary_key = True)
    part_id = db.Column(db.Integer,db.ForeignKey("parts.id"))
    process_name = db.Column(db.String(64))
    process_content = db.Column(db.String(64))
    working_hours = db.Column(db.Numeric(precision=3,scale=2))
    process_resources = db.Column(db.String(64))

    def __unicode__(self):
        return self.process_name

    def __repr__(self):
        return '<Process %r>' % (self.process_name)




