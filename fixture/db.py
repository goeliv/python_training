import mysql.connector

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self. ser = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)

    def destroy(self):
        self.connection.close()

