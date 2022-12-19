class Student():

    id = 100001
    university  = "UEK Kraków"

    def __init__(self, name, surname, field_of_study):
        self.name = name
        self.surname = surname
        self.field_of_study = field_of_study
        self.id = Student.id
        Student.id += 1
        


    
    def __str__(self):
        return f"{self.name}  {self.surname} {self.id}, {self.field_of_study}, {Student.university}"


s1 = Student("Anna", "MAJ","Applied Informatics")
print(s1)
print()
s2 = Student("Jan", "KOWALSKI","Informatyka stosowana")
print(s2)
print()
