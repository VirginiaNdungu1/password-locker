import unittest

from pwd_locker import Users


class TestPwdLocker(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
