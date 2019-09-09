def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }
    if songs:
        album["songs"] = songs
    return album


artist = ""
title = ""
songs = None

while True:
    artist = input("Who is the artist?\n")
    if artist.lower() == "quit":
        break
    title = input("What is the title?\n")
    songs = input("How many songs?\n")
    print(make_album(artist, title, songs))



