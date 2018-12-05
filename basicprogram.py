from soundcloud_playlist import Playlist


def Main():
    play = Playlist('D:/chromedriver/chromedriver.exe', 'https://soundcloud.com/aetherboy1/lil-peep-crybaby-aetherboy1-flip', "new_3")
    play.start()
    x = input("Zalogowales sie i stworzyles playliste? y/n: ")
    if x =="y":
        play.go_to_song()
        play.next_songs()


if __name__ == '__main__':
    Main()
