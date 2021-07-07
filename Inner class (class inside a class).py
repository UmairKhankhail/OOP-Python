class Human:  #outer class

    def __init__(self,name,age):
        self.Name=name
        self.Age=age
        self.laptop=self.Laptop()    
    def GetInformation(self):
        return "{} {}".format(self.Name,self.Age)

    class Laptop:

        def __init__(self):
            self.Type="Dell"
            self.CPU="Core-i7"

        def GetLaptopInfo(self):
            return "{} {}".format(self.Type,self.CPU)

h1=Human('Hamza',20)
print(h1.GetInformation())
print(h1.laptop.GetLaptopInfo())