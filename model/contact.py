from sys import maxsize
class Contact:

    def __init__(self, firstname=None, lastname=None, nick=None, middlename=None, title=None, company=None, address=None, home_tel=None, mob_tel=None,
                                work_tel=None, fax=None, email=None, email2=None, homepage=None, birthday=None, id=None, secondary_tel=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nick = nick
        self.title = title
        self.company = company
        self.address = address
        self.home_tel = home_tel
        self.mob_tel = mob_tel
        self.work_tel = work_tel
        self.secondary_tel = secondary_tel
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.homepage = homepage
        self.birthday = birthday
        self.id = id
        self.all_phones_from_home_page=all_phones_from_home_page
        self.all_emails_from_home_page=all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.middlename, self.nick, self. title, self. company, self.address, self.home_tel, self.mob_tel)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize







