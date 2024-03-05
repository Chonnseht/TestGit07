class Vinyl:
    def __init__(self, album, artist, year):
        self.album = album
        self.artist = artist
        self.year = year

    def display(self):
        print(self.album + " by " + self.artist + " released on " + self.year)


born_this_way = Vinyl("Born This Way", "Lady Gaga", "2011")

born_this_way.display()
