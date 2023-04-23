class Connection:

    user: str
    password: str
    # private attribute
    _hash: str
    
    @classmethod
    def create_default_connection(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        connection._hash = '$#*4HW@#$&HD@$&@D'
        return connection
    

    @staticmethod
    def log(msg):
        print('log: ', msg)

    # getter
    @property
    def get_user(self):
        return self.user
    
    # setter
    # @user.setter
    def user(self, user):
        print('setter')
        self.user = user


c1 = Connection.create_default_connection('vinicius','123')
print(c1.user, c1.password, c1._hash)

Connection.log('Teste')


c2 = Connection()
c2.user = 'Test'
c2.password = '123'
print(c2.user, c2.password)
print(c2.get_user)


