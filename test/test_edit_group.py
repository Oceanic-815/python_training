# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_edit_first_group(app, db):
    group = Group(name="New group", header="added header", footer="added footer")
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    #assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# after 'group = random'
# index = randrange(len(old_groups))
# group.id = old_groups[index].id
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