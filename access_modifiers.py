class Student:
    
    __name = None # Private Data Member / Attribute
    _age = None   # Protected Data Member / Attribute
    dob = None    # Public Data Member / Attribute

    def __init__(self):
        self.__name = "Tabish"
        self._age = "21"
        self.dob = "2xxx"

    def output(self):
        print(f"Parent Class:\n Name (Private) = {self.__name}\n Age (Protected) = {self._age}\n DOB (Public) = {self.dob}\n")

class ChildStudent(Student):
        
    def __init__(self):
        Student.__init__(self)  
    
    def printChild(self):
        #print(f"Child - Age: {self.__name}")
        print(f"Child Class:\n Name (Private) = not accessible")
        print(f" Age (Protected): {self._age}")
        print(f" DOB (Public): {self.dob}")
        

s1 = Student()
s1.output()

print(f"Accessing Public Data Member from object/ instance of Student Class\n DOB: {s1.dob} \n")

print("----------------------------------------------------------\n")


s2 = ChildStudent()
s2.printChild()
