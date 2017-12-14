import unittest
from main_menu import Main_menu


class TestMainMenu(unittest.TestCase):
    def setUp(self):
        self.main_menu = Main_menu()

    def test_constructor(self):
        self.assertEqual(self.main_menu._play_all, 1)
        self.assertEqual(self.main_menu._create_playlist, 2)
        self.assertEqual(self.main_menu._play_playlist, 3)
        self.assertEqual(self.main_menu._add_to_existing, 4)
        self.assertEqual(self.main_menu._search_by_song, 5)
        self.assertEqual(self.main_menu._search_by_method, 6)
# can't figure out how to simulate test for user input successfully
# had to do by hand


if __name__ == '__main__':
    unittest.main()