class Student():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def __str__(self):
        return f"Imię: {self.name}, Oceny: {self.grades}"

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return round(sum(self.grades)/len(self.grades),2)
    
    def passed(self):
        if round(sum(self.grades)/len(self.grades),2) >= 3.0:
            return f"Nice, mission completed"
        else:
            return f"Close one"
Maciej = Student("Maciej", [4, 2, 4, 3, 5, 3])
print(Maciej)
Maciej.add_grade(4)
print(Maciej)
print(Maciej.average())
print(Maciej.passed())