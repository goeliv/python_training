from model.group import Group
from random import randrange


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="dfgdfg", header="dfgdfgd", footer="dfgdfgdfg"))
    old_groups=app.group.get_group_list()
    index = randrange (len(old_groups))
    group = Group(name="new", header="new", footer="new")
    group.id=old_groups[index].id
    app.group.modify_by_index(index, group)
    new_groups=app.group.get_group_list()
    assert len(old_groups)== len (new_groups)
    old_groups[index]= group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
