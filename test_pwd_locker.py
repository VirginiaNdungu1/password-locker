import unittest

from pwd_locker import User


class TestPwdLocker(unittest.TestCase):
    def setUp(self):
        self.new_user = User(1, "Virginia", "nish", 12345)

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
        self.assertEqual(len(User.user_list), 1)


if __name__ == "__main__":
    unittest.main()
