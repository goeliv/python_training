from model.group import Group
from random import randrange


def test_modify_first_group(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contact(firstname="test", middlename="test", lastname="gkhgkg", nick="gkgkgk", title="gkgk", company="gkgkjgkgk", address="gkgkjgkgk", home_tel="777", mob_tel="888",
                                work_tel="999", fax="777", email="2532@AMAI.COM", email2="2515832@AMAI.COM", homepage="ppp.com", birthday="1989"))
        old_groups=app.group.get_group_list()
        index = randrange (len(old_groups))
        group = Group(name="new", header="new", footer="new")
        group.id=old_groups[index].id
        app.group.modify_by_index(Group(index, group))
        new_groups=app.group.get_group_list()
        assert len(old_groups)== len (new_groups)
        old_groups[index]= group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
