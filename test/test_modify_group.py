from model.group import Group
import random


def test_modify_some_group(app, db, check_ui):
    if len (db.get_group_list())== 0:
        app.group.create(Group(name="1", header="1", footer="1"))
    old_groups=db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_by_id(id, group)
    new_groups=db.get_group_list()
    assert len(old_groups)== len (new_groups)
    old_groups[id]= group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

