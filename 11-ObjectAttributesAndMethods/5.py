class music():

    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.title = track_title
        self.album = album
        self.year = year
    
    def __str__(self):
        return (f"Performer: {self.artist}\nSong:      {self.title}\nAlbum:      {self.album}\nYear:       {self.year}")


m1 = music('Ed sheeran', "Hearts Don't Break Around here", "Divide", 2017)
print(m1)
print()
m2 = music("JWP", "Byc tam", "Wróg publiczny numer 1", 2004)
print(m2)
print()
m3 = music("Arctic Monkeys", "Do I wanna know", "album1", 2015)
print(m3)

x = 1

print(type(x))