def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }
    if songs:
        album["songs"] = songs
    return album


print(make_album("dylan", "album", 10))
print(make_album("bob", "cool guy"))

