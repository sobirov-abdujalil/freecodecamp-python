# Workshop: Build a Media Catalogue
class Media:
    def __init__(self, title, year):
        self.title = title
        self.year = year

class Book(Media):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages

class Movie(Media):
    def __init__(self, title, year, director, duration):
        super().__init__(title, year)
        self.director = director
        self.duration = duration

class Catalogue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def search_by_year(self, year):
        return [i for i in self.items if i.year == year]
