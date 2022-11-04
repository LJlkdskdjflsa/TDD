from dataclasses import dataclass

@dataclass
class Movie(object):
    _copies: int = 0
    
    def add_copies(self):
        self._copies += 1

    def get_copies(self):
        return self._copies
    
class Library(object):
    def __init__(self):
        self._catalogue = []

    def donate(self,movie:Movie):
        self._catalogue.append(movie)
        movie.add_copies()

    def contains(self, movie: Movie):
        return movie in self._catalogue

    
    def get_catalogue(self):
        return self._catalogue

    