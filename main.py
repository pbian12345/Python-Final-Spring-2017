from song_player import SongPlayer
from main_menu import Main_menu
from pygame import *

def start_app():
    print("Please enter name of user:")
    player_name = input("> ")
    player = SongPlayer(player_name)
    menu = Main_menu()
    print("At any time, if you want to exit this program,")
    print("simply enter 'x' when prompted.")

    print("Is there a method that you would like to be able")
    print("to use to search your songs other than by song?")
    print("I.e. artist, genre, album, etc.")
    print("Please enter the method or enter 'no'")
    method_type = input("> ")
    player.end_program(method_type)
    if method_type != "no":
        player.create_playlist(method_type)
        # Making it so it will work regardless of songs in song_files, but then can't make classes for each song
        # containing various attributes like artist and genre based only on the mp3 files' names.
        # I would need more data than just the files, especially since these files will most likely be
        # downloaded from youtube. The data in files obtained legit contain that data.


    user_input = menu.menu(method_type)
    player.end_program(user_input)

    while user_input != 'x' or user_input != "X":
        if user_input == "1":
            player.play_playlist("all_songs")
            user_input = menu.menu(method_type)
            player.end_program(user_input)
        elif user_input == "2":
            print("What would you like to name your new playlist?")
            new_playlist = input("> ")
            player.end_program(new_playlist)
            player.create_playlist(new_playlist)
            user_input = menu.menu(method_type)
            player.end_program(user_input)
            # must input name of playlist w/o .txt
        elif user_input == "3":
            print("Please enter name of desired playlist:")
            playlist_name = input("> ")
            player.end_program(playlist_name)
            player.play_playlist(playlist_name)
        elif user_input == "4":
            print("To what playlist do you want to add a song?")
            playlist_add_to = input("> ")
            player.end_program(playlist_add_to)
            print("What song would you like to add to", playlist_add_to + "?")
            song_name = input("> ")
            player.end_program(song_name)
            player.add_to_playlist(playlist_add_to, song_name)
        elif user_input == "5":
            print("What song would you like to search for?")
            song_name = input("> ")
            player.end_program(song_name)
            song_search_file = open("playlists/all_songs.txt", "r")
            for line in song_search_file:
                if song_name in line:
                    player.play_song(line)
                    print("Enter 1 to pause, 2 to stop, 3 to skip, 4 to like")
                    user_input = input("> ")
                    player.end_program(user_input)
                    if user_input == 1:
                        mixer.music.pause()
                    elif user_input == 2:
                        mixer.music.stop()
                        break
                    elif user_input == 3:
                        mixer.music.stop()
                    elif user_input == 4:
                        player.like_song(line)
                    break
        elif user_input == "6":
            print("All inputted songs matching", method_type, "are listed below.")
            method_playlist_file = open("playlist/" + method_type + ".txt", "r")
            for line in method_playlist_file:
                print(line)
            print("Please enter name of song you would like to listen to, or enter 'play all'")
            song_name = input("> ")
            player.end_program(song_name)
            if song_name == "play all":
                player.play_playlist(method_type)
            else:
                player.play_song(song_name)



if __name__ == '__main__':
    start_app()