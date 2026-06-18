class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer (Employee):
    def showLanguage(self):
        print("The Default language is Python")

e1 = Employee("Mohan Dhanu" , 600)
e1.showDetails()
e2 = Programmer ("Mili" , 400)
e2.showDetails()
e2.showLanguage()