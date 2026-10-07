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

Pan_Tadeusz = Book("Pan Tadeusz", "Adam Mickiewicz", 1834, "Epopeja narodowa opisująca życie polskiej szlachty na Litwie na początku XIX wieku, ukazująca konflikty, tradycje i dążenia niepodległościowe")
Odyseja = Book("Odyseja", "Homer", -800, "Epos grecki opowiadający o dziesięcioletniej wędrówce Odyseusza wracającego do Itaki po wojnie trojańskiej, pełnej przygód, mitologicznych istot i prób charakteru.")
print(Pan_Tadeusz.info())
print(Odyseja.info())
print(Pan_Tadeusz.compare(Odyseja))