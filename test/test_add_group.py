# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="3333", header="3333", footer="3333"))

def test_add_empty_group(app):
   app.group.create(Group(name="", header="", footer=""))
