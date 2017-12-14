import unittest
from user import User

class UserTest(unittest.TestCase):

    def test_adding_to_playist(self):
        user = User("Pierson")
        self.assertEqual(user.username, "Pierson")

if __name__ == '__main__':
    unittest.main()