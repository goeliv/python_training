from model.group import Group

def test_modify_first_group(app):
    if app.group.count()==0:
        app.group.create(Group(name="1", header="1", footer="1"))
        app.group.modify(Group(name="new", header="new", footer="new"))
