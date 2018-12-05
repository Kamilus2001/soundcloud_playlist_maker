from soundcloud_playlist import Playlist


def Main():
    play = Playlist('chromedriver location', 'link to your track', "name of ur sc playlist")
    play.start()
    x = input("Have you logged in and create a playlist? y/n: ")
    if x =="y":
        play.go_to_song()
        play.next_songs()


if __name__ == '__main__':
    Main()
