import unittest

from pwd_locker import Credentials, Users


class TestPwdLocker(unittest.TestCase):
    def setUp(self):
        self.new_user = Users(1, "Virginia", "nish", 12345)
        self.new_account = Credentials(
            1, "Github", "ndungu.wairimu22@gmail.com", "VirginiaNdungu1", "xyz123")

    def test_init(self):
        '''
        test if User Object has been properly initialised
        '''
        self.assertEqual(self.new_user.user_id, 1)
        self.assertEqual(self.new_user.fullname, "Virginia")
        self.assertEqual(self.new_user.username, "nish")
        self.assertEqual(self.new_user.user_password, 12345)
        '''
        test if Credentials Object has been properly initialised
        '''
        self.assertEqual(self.new_account.acc_id, 1)
        self.assertEqual(self.new_account.acc_name, "Github")
        self.assertEqual(self.new_account.acc_email,
                         "ndungu.wairimu22@gmail.com")
        self.assertEqual(self.new_account.acc_username, "VirginiaNdungu1")
        self.assertEqual(self.new_account.acc_password, "xyz123")

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

    def test_check_display_users(self):
        '''
        test to check if all users in user_list are displayed
        '''
        self.new_user.save_user()
        test_user = Users(2, "Mbugua", "gitu", 467587)
        test_user.save_user()
        self.assertEqual(Users.display_users(), Users.user_list)

    def test_check_authenticate_user(self):
        '''
        test to authenticate user
        '''
        self.new_user.save_user()
        test_user = Users(2, "Mbugua", "gitu", 467587)
        test_user.save_user()
        user_authenticated = Users.authenticate_user(1, "nish", 12345)
        self.assertTrue(user_authenticated)


if __name__ == "__main__":
    unittest.main()
