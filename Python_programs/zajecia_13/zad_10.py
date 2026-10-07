class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def __str__(self):
        return f"Imię: {self.name}, Wypłata: {self.get_salary()} zł"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary) 
        self.bonus = bonus

    def get_salary(self):
        return self.salary + self.bonus

    def __str__(self):
        return f"Stanowisko: Manager, Imię: {self.name}, Wypłata: {self.get_salary()}zł"

Maciej = Employee("Jan Kowalski", 4000)

Michał = Manager("Anna Nowak", 6000, 1500)

print(Maciej)
print(Michał)

print(f"Maciej dostaje: {Maciej.get_salary()}zł")
print(f"Michał dostaje: {Michał.get_salary()}zł")