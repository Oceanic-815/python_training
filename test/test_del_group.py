from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="just added", header="just added", footer="just added"))
    app.group.delete_first_group()
