import unittest
from song_player import SongPlayer


class TestSongPlayer(unittest.TestCase):
    def setUp(self):
        self.player = SongPlayer("Pierson")
        # User input in constructor makes this test really troublesome

    def test_create_of_songplayer(self):
        self.assertEqual(self.player.user.username, "Pierson")

# This test will loop infinitely without user input
    # def test_create_playlist(self):
    #     self.assertEqual(self.player.create_playlist("Dude"), True)

    def test_add_to_playlist(self):
        self.assertEqual(self.player.add_to_playlist("Dude", "Mary"), True)

# These tests pass, but will have to listen to whole song through
    # def test_play_song(self):
    #     self.assertEqual(self.player.play_song("Why Should I Worry.mp3"),True)

    # def test_play_song_for_playlist(self):
    #     self.assertEqual(self.player.play_song_for_playlist("Vienna.mp3"), True)

    # def test_play_playlist(self):
    #     self.assertEqual(self.player.play_playlist("all_songs"), True)

    def test_like_song(self):
        self.assertEqual(self.player.like_song("I Did It"), True)

    def test_end_program(self):
        with self.assertRaises(SystemExit):
            self.player.end_program("x")
        self.assertEqual(self.player.end_program("blah"), 0)

if __name__ == '__main__':
    unittest.main()
