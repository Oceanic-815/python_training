# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="just added", header="just added", footer="just added"))
    app.group.edit_first_group(Group(name="New group"))

def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="just added", header="just added", footer="just added"))
    app.group.edit_first_group(Group(header="New header"))
