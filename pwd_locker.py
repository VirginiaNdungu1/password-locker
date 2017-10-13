class Users:

    user_list = []

    def __init__(self, user_id, fullname, username, user_password):
        '''
        Initialise User Object
        '''
        self.user_id = user_id
        self.fullname = fullname
        self.username = username
        self.user_password = user_password

    def save_user(self):
        '''
        Save User object in user_list
        '''
        Users.user_list.append(self)

    @classmethod
    def find_user_by_id(cls, user_id):
        for user in cls.user_list:
            if user.user_id == user_id:
                return user

    @classmethod
    def check_user_existence(cls, user_id):
        for user in cls.user_list:
            if user.user_id == user_id:
                return True

        return False
