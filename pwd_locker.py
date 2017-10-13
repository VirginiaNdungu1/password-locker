class User:

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
        User.user_list.append(self)
