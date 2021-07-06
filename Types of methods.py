# Methods are of three types Instance method, class method and Instance method

#Instance method

class Student:
    

   #class/static variable
    
    school="NEDUET"

    def __init__(self,m1,m2,m3,m4):
        
        #Instance Variables
        self.M1=m1
        self.M2=m2
        self.M3=m3
        self.M4=m4
    
    #This is instance varible because we are passing self parameter in it and it can be accessed only thruogh object. It can not be accessed through class
    def GetAverage(self):
        return (self.M1+self.M2+self.M3+self.M4)/4

    #These getter and setter are also instance variables
    def SetValue(self,m):
        self.M1=m
    def GetValue(self):
        return self.M1
    
    # Class Methods

    #This is class method with the help of this we can manipulate and access class variables. In his function we pass cls as a parameter in place of self.
    # we can access class methods through both objects and class

    @classmethod #-------> Decorator
    def GetCollege(cls):
        return cls.school

    # Static Methods

    # static methods neither belongs to class nor object. They can be accessed through both class and object. They are like normal funcitons.

    @staticmethod
    def factorial():
        print("This is static method for factorial.")

s1=Student(40,50,60,30)
print(s1.GetAverage())
s1.SetValue(100)
print(s1.GetAverage())
print(s1.school)
print("class method called through class: ",Student.GetCollege())
print("class method called through object: ",s1.GetCollege())
Student.factorial()
s1.factorial()