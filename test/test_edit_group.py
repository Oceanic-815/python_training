# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New group", header="added header", footer="added footer")
    if app.group.count() == 0:
        app.group.create(group)#(Group(name="just added", header="just added", footer="just added"))
    group.id = old_groups[0].id
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

"""
def test_edit_first_group_header(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New header")
    if app.group.count() == 0:
        app.group.create(Group(name="just added", header="just added", footer="just added"))
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""