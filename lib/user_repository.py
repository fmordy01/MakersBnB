from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        return [User(row['id'], row['username'], row['email'], row['password'])
                for row in rows]
