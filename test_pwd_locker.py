import random
import string
import unittest

from pwd_locker import Credentials, Users


class TestPwdUsers(unittest.TestCase):
    def setUp(self):
        self.new_user = Users(1, "Virginia", "nish", 12345)

    def test_init(self):
        '''
        test if User Object has been properly initialised
        '''
        self.assertEqual(self.new_user.user_id, 1)
        self.assertEqual(self.new_user.fullname, "Virginia")
        self.assertEqual(self.new_user.username, "nish")
        self.assertEqual(self.new_user.user_password, 12345)

    def test_save_user(self):
        '''
        test if User object has been saved in user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(Users.user_list), 1)

    def tearDown(self):
        '''
        tearDown cleans up after each test case runs
        '''
        Users.user_list = []

    def test_save_multiple_users(self):
        '''
        test if multiple user objects have been saved in user_list
        '''
        self.new_user.save_user()
        test_user = Users(2, "Mbugua", "gitu", 467587)
        test_user.save_user()
        self.assertEqual(len(Users.user_list), 2)

    def test_find_user_by_id(self):
        '''
        test to ensure we can find a user by their ID and access their details
        '''
        self.new_user.save_user()
        test_user = Users(2, "Mbugua", "gitu", 467587)
        test_user.save_user()
        search_user = Users.find_user_by_id(2)
        self.assertEqual(search_user.username, test_user.username)

    def test_check_user_existence(self):
        '''
        test to check if user exists in user_list
        '''
        self.new_user.save_user()
        test_user = Users(2, "Mbugua", "gitu", 467587)
        test_user.save_user()
        user_exists = Users.check_user_existence(2)
        self.assertTrue(user_exists)

    def test_check_authenticate_user(self):
        '''
        test to authenticate user
        '''
        self.new_user.save_user()
        test_user = Users(2, "Mbugua", "gitu", 467587)
        test_user.save_user()
        user_authenticated = Users.authenticate_user(1, "nish", 12345)
        self.assertTrue(user_authenticated)

    def test_check_display_users(self):
        '''
        test to check if all users in user_list are displayed
        '''
        self.new_user.save_user()
        test_user = Users(2, "Mbugua", "gitu", 467587)
        test_user.save_user()
        self.assertEqual(Users.display_users(), Users.user_list)


class TestPwdCredentials(unittest.TestCase):

    def setUp(self):
        self.new_user = Users(1, "Virginia", "nish", 12345)
        self.new_account = Credentials(
            1, "Github", "ndungu.wairimu22@gmail.com", "VirginiaNdungu1", "xyz123")

    def test_init(self):
        '''
        test if Credentials Object has been properly initialised
        '''
        self.assertEqual(self.new_account.acc_id, 1)
        self.assertEqual(self.new_account.acc_name, "Github")
        self.assertEqual(self.new_account.acc_email,
                         "ndungu.wairimu22@gmail.com")
        self.assertEqual(self.new_account.acc_username, "VirginiaNdungu1")
        self.assertEqual(self.new_account.acc_password, "xyz123")

    # def test_check_authenticate_user(self):
    #     '''
    #     test to authenticate user
    #     '''
    #     self.new_user.save_user()
    #     test_user = Users(2, "Mbugua", "gitu", 467587)
    #     test_user.save_user()
    #     user_authenticated = Users.authenticate_user(1, "nish", 12345)
    #     self.assertTrue(user_authenticated)
    def test_acc_password(self, size=10, char=string.ascii_lowercase + string.digits):
        '''
        Generate a random password
        '''
        acc_password = ''.join(random.choice(char) for _ in range(size))
        return acc_password
        self.assertEqual(Credentials.acc_password, new_account.acc_password)

    def test_save_account(self):
        '''
        test if account is saved to account_list
        '''
        self.new_account.save_account()
        self.assertEqual(len(Credentials.account_list), 1)

    def tearDown(self):
        '''
        tearDown cleans up after each test case runs
        '''
        Credentials.account_list = []

    def test_save_multiple_accounts(self):
        '''
        test if multiple Credentials objects have been saved in account_list
        '''
        self.new_account.save_account()
        test_account = Credentials(
            2, "Slack", "ndungu.wairimu22@gmail.com", "monster", "467K587")
        test_account.save_account()
        self.assertEqual(len(Credentials.account_list), 2)

    # def test_gen_random_pwd

    def test_find_account_by_id(self):
        '''
        test to ensure we can find a credential by their ID and access their details
        '''
        self.new_account.save_account()
        test_account = Credentials(
            2, "Slack", "ndungu.wairimu22@gmail.com", "monster", "467K587")
        test_account.save_account()
        search_account = Credentials.find_account("Slack")
        self.assertEqual(search_account.acc_name, test_account.acc_name)

    def test_check_account_existence(self):
        '''
        test to check if credential exists in account_list
        '''
        self.new_account.save_account()
        test_account = Credentials(
            2, "Slack", "ndungu.wairimu22@gmail.com", "monster", "467K587")
        test_account.save_account()
        account_exists = Credentials.check_account_existence("Slack")
        self.assertTrue(account_exists)

    def test_display_accounts(self):
        '''
        test to check if all credential objects in account_list are displayed
        '''
        self.new_account.save_account()
        test_account = Credentials(
            2, "Slack", "ndungu.wairimu22@gmail.com", "monster", "467K587")
        test_account.save_account()
        self.assertEqual(Credentials.display_accounts(),
                         Credentials.account_list)


if __name__ == "__main__":
    unittest.main()
