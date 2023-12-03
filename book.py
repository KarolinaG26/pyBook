class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Ksiazka: {self.title} Autor: {self.author} Rok: {self.year}"
    def chage_title(self, new_title):
        self.title = new_title
    def chage_author(self, new_author):
        self.author = new_author

    def change_year(self, new_year):
        self.year = new_year


#book = Book("Wiedzmin", "AS", 2000)
#print(book.get_info())