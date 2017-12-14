
class Main_menu(object):
    def __init__(self):
        self._play_all = 1
        self._create_playlist = 2
        self._play_playlist = 3
        self._add_to_existing = 4
        self._search_by_song = 5
        self._search_by_method = 6

    def menu(self, method):
        print("Main menu:")
        print("1: play all songs")
        print("2: create new playlist")
        print("3: play playlist")
        print("4: add to existing playlist")
        print("5: search by song")
        print("6: search by", method)
        user_input = input("> ")
        return user_input