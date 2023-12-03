class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Ksiazka: {self.title} Autor: {self.author} Rok: {self.year}"

book = Book("Wiedzmin", "AS", 2000)
print(book.get_info())