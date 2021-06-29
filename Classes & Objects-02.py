#We write the names of function or classes in the following styles
#Snake Case: function_name -------> Used for methods
#Camel Case: functionName ------> Used 
#Pascal Case: FunctionName -----> Used for classes

l=[1,8,2,3,4,5,6]
print(type(l))
l.sort() #Here the sort is a method of list class, that is why it is called with dot(.) after an object of list class
print(l)

#list etc. are built-in classes

#variable_name=variable updates the value if the value already exists
#referce_variable.attribute_name=value updates the attribute already

class Car():
      
    def SetType(self,type):
         self.Type=type
    def GetType(self):
        return self.Type

    def SetModel(self,model):
        self.Model=model
    def GetModel(self):
        return self.Model

    def SetPrice(self,price):
        self.Price=price
    def GetPrice(self):
        return self.Price

    def SetMiles(self,miles):
        self.Miles=miles
    def GetMiles(self):
        return self.Miles

    def GetCurrentPrice(self):
        return self.Price-(self.Miles*10)

car1=Car()
car1.SetType('BMW')
car1.SetModel(2020)
car1.SetPrice(10000000)
car1.SetMiles(20)

car2=Car()
car2.SetType('Carolla')
car2.SetModel(2021)
car2.SetPrice(200000)
car2.SetMiles(40)

car3=Car()
#Now if i do not set its methods, it won't give any value instead it will give an error

#To get id's of different object to find wheather they are on same place or not
print(id(Car))
print(id(car1))
print(id(car2))
print(id(car3))


print(car1.GetCurrentPrice())    
print(car2.GetCurrentPrice())

