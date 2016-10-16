
from model.group import Group

def test_delete_first_group(app):
    if app.group.count()==0:
        app.group.create(Group(name="1", header="1", footer="1"))
        app.group.delete_first_group()

