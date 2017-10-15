import random
import string

global user_list


class Users:

    user_list = []
    # user_credentials = dict(username,)

    def __init__(self, user_id, fullname, username, user_password):
        '''
        Initialise User Object
        '''
        self.user_id = user_id
        self.fullname = fullname
        self.username = username
        self.user_password = user_password
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

    @classmethod
    def authenticate_user(cls, user_id, username, user_password):
        confirm_user_exists = cls.check_user_existence(user_id)
        for user in cls.user_list:
            if confirm_user_exists == True and (user.username == username and user.user_password == user_password):
                return True
        return False

    @classmethod
    def display_users(cls):
        return cls.user_list


class Credentials:
    global user_list
    account_list = []

    def __init__(self, acc_id, acc_name, acc_email, acc_username, acc_password):
        '''
        Initialise Accounts Object
        '''
        self.acc_id = acc_id
        self.acc_name = acc_name
        self.acc_email = acc_email
        self.acc_username = acc_username
        self.acc_password = acc_password

    # # @classmethod
    # def authenticate_user(self, user_id, username, user_password):
    #     confirm_user_exists = Users.check_user_existence(user_id)
    #     for user in Users.user_list:
    #         if confirm_user_exists == True and (user.username == username and user.user_password == user_password):
    #             return True
    #     return False

    def acc_password(self, size=10, char=string.ascii_lowercase + string.digits):
        '''
        Generate a random password
        '''
        acc_password = ''.join(random.choice(char) for _ in range(size))
        return self.acc_password

    def save_account(self):
        '''
        Create and save account in account_list
        '''
        Credentials.account_list.append(self)

    @classmethod
    def find_account_by_id(cls, acc_id):
        for account in cls.account_list:
            if account.acc_id == acc_id:
                return account

    @classmethod
    def check_account_existence(cls, acc_id):
        for account in cls.account_list:
            if account.acc_id == acc_id:
                return True

        return False

    @classmethod
    def display_accounts(cls):
        return cls.account_list
