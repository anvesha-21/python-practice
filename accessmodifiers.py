class Student :
    def __init__(self):
        self._name = "Tangy"

    def _funName(self):
        return "Mangy"
    
class Subject (Student):
    pass

obj =Student()
obj1 = Subject()

print(obj._name)
print(obj._funName())

print(obj1._name)
print(obj1._funName())

