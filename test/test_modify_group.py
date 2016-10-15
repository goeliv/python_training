from model.group import Group

def test_modify_first_group(app):
    app.group.modify(Group(name="new", header="new", footer="new"))
