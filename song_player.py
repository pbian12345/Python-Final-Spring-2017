import os, sys
from user import User
from pygame import *

class SongPlayer(object):
    def __init__(self, username):
        self.user = User(username)
        print("Hello,", username + ".")
        print("Would you like to reset your playlists? (y/n)")
        user_input = input("> ")
        self.end_program(user_input)
        if user_input == "y":
            self.reset_playlists()

        all_songs_file = open("playlists/" + "all_songs.txt", "w")
        all_songs_file.truncate()
        for file_name in os.listdir("song_files"):
            all_songs_file.write(file_name + "\n")
        all_songs_file.close()

        fav_file = open("playlists/favorites.txt", "w")
        fav_file.close()

    def reset_playlists(self):
        for file in os.listdir("playlists"):
            os.remove("playlists/" + file)

    def create_playlist(self, playlist_name):
        playlist_file = open("playlists/" + playlist_name + ".txt", "w")
        check_file = open("playlists/all_songs.txt", "r")
        print("To stop adding songs, enter '*finished'")
        print("Input must be identical to audio file name.")
        user_input = ""
        while user_input != "*finished":
            print("Enter song name, or enter '*finished'")
            user_input = input("> ")
            self.end_program(user_input)
            if user_input + "\n" not in check_file:
                print("Error: song not found.")
            else:
                playlist_file.write(user_input + "\n")
                print(user_input, "added to", playlist_name, "playlist.")
        playlist_file.close()
        check_file.close()
        return True

    def add_to_playlist(self, playlist_name, song_name):
        # If playlist doesn't exist, will create it.
        playlist_file = open("playlists/" + playlist_name + ".txt", "w")
        check_file = open("playlists/all_songs.txt", "r")
        if song_name + "\n" not in check_file:
            print("Error: song not found.")
        playlist_file.write(song_name + "\n")
        playlist_file.close()
        print(song_name, "added to", playlist_name, "playlist.")
        return True

    def play_playlist(self, playlist_name):
        playlist_file = open("playlists/" + playlist_name + ".txt")
        for line in playlist_file:
            type_of_stop = self.play_song_for_playlist(line)
            if type_of_stop == 1:
                break
        return True

    def play_song_for_playlist(self, song_name):
        song_name = song_name.rstrip()
        mixer.init()
        mixer.music.load("song_files/" + song_name)
        mixer.music.play()
        print("Enter 1 to stop, 2 to skip, 3 to like")
        new_user_input = input("> ")
        self.end_program(new_user_input)
        if new_user_input == "1":
            mixer.music.stop()
            return 1
        elif new_user_input == "2":
            mixer.music.stop()
            return
        elif new_user_input == "3":
            self.like_song(song_name)
        while mixer.music.get_busy():
            time.Clock().tick(10)
        return True

    def play_song(self, song_name):
        song_name = song_name.rstrip()
        mixer.init()
        mixer.music.load("song_files/" + song_name)
        mixer.music.play()
        while mixer.music.get_busy():
            time.Clock().tick(10)
        return True

    def like_song(self, song_name):
        self.add_to_playlist("favorites", song_name)
        self.add_to_playlist("all_songs", song_name)
        return True

    def end_program(self, user_input):
        if user_input == "x" or user_input == "X":
            print("Goodbye,", self.user.username + ".")
            sys.exit(0)
        else:
            return 0