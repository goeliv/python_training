from model.group import Group
from random import randrange


def test_modify_some_group(app, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="1", header="1", footer="1"))
    old_groups=app.group.get_group_list()
    index = randrange (len(old_groups))
    group = Group(name="new", header="new", footer="new")
    group.id=old_groups[index].id
    app.group.modify_by_index(index, group)
    new_groups=app.group.get_group_list()
    assert len(old_groups)== len (new_groups)
    old_groups[index]= group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

