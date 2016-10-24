from model.group import Group

def test_modify_first_group(app):
    old_groups=app.group.get_group_list()
    group = Group(name="new", header="new", footer="new")
    group.id=old_groups[0].id
    app.group.modify(Group(name="new", header="new", footer="new"))
    new_groups=app.group.get_group_list()
    assert len(old_groups)== len (new_groups)
    old_groups[0]= group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
