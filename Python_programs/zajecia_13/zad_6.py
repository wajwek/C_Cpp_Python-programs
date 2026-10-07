class Book():
    def __init__(self, title, author, year, description):
        self.title = title
        self.author = author
        self.year = year
        self.description = description
    
    def __str__(self):
        return f"Tutuł: {self.title}, Autor: {self.author}, Rok wydania:{self.year}"

    def info(self):
        return f"Tutuł: {self.title}, Autor: {self.author}, Rok wydania:{self.year}\n Opis:\n {self.description}"
    
    def compare(book1, book2):
        if book1.year == book2.year:
            return f"Ten sam rok wydania"
        else:
            return f"Inny rok wydania"

class Library():
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        found = False
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Usunięto książkę: {title}")
                found = True
                break 
        
        if not found:
            print(f"Nie znaleziono książki o tytule: {title}")

    def search_by_author(self, author):
        print(f"Książki autora: {author}")
        count = 0
        for book in self.books:
            if book.author == author:
                print(book)
                count += 1
    
        if count == 0:
            print("Brak książek tego autora.")

    def show_all_books(self):
        for book in self.books:
            print(book)

Pan_Tadeusz = Book("Pan Tadeusz", "Adam Mickiewicz", 1834, "Epopeja narodowa opisująca życie polskiej szlachty na Litwie na początku XIX wieku, ukazująca konflikty, tradycje i dążenia niepodległościowe")
Odyseja = Book("Odyseja", "Homer", -800, "Epos grecki opowiadający o dziesięcioletniej wędrówce Odyseusza wracającego do Itaki po wojnie trojańskiej, pełnej przygód, mitologicznych istot i prób charakteru.")

mojabiblioteka = Library()
mojabiblioteka.add_book(Pan_Tadeusz)
mojabiblioteka.add_book(Odyseja)
print()
mojabiblioteka.show_all_books()
print()
mojabiblioteka.search_by_author("Homer")
print()
mojabiblioteka.remove_book("Pan Tadeusz")
print()
mojabiblioteka.show_all_books()