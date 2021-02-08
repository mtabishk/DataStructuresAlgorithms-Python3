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

class ChildStudentA(Student):
        
    def __init__(self):
        Student.__init__(self)  
    
    def printChild(self):
        # Accessing Instance Variables
        print(f"Child Class A,  Accessing Instance Variables:\n Name (Private) = not accessible")
        print(f" Age (Protected): {self._age}")
        print(f" DOB (Public): {self.dob}")
        

class ChildStudentB(Student):
        
    def __init__(self):
        #super().__init__()  # Using initializer of parent class
        pass
    
    def printChild(self):
        # Accessing Class Variables
        print(f"Child Class B Accessing Class Variables:\n Name (Private) = not accessible")
        print(f" Age (Protected): {Student._age}")
        print(f" DOB (Public): {Student.dob}")


s1 = Student()
s1.output()

print(f"Accessing Public Data Member from object/ instance of Student Class\n DOB: {s1.dob} \n")

print("----------------------------------------------------------\n")


s2 = ChildStudentA()
s2.printChild()

print("----------------------------------------------------------\n")

s3 = ChildStudentB()
s3.printChild()