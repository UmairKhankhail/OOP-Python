class Car():

    def SetName(self,name):
        self.Name=name

    def SetModel(self,model):
        self.Model=model

    def SetSize(self,size):
        self.Size=size
    
    def SetColor(self,color):
        self.Color=color
    
    def SetPrice(self,price):
        self.Price=price
    
    def GetInformation(self):
        return self.Name+'\n'+self.Model+'\n'+self.Size+'\n'+self.Color+'\n'+self.Price

car1=Car()
car1.SetName('Pajero')
car1.SetModel('2016')
car1.SetSize('Medium')
car1.SetColor('Black')
car1.SetPrice('Rs 15000')

car2=Car()
car2.SetName('Suzuki')
car2.SetModel('2020')
car2.SetSize('Large')
car2.SetColor('Red')
car2.SetPrice('Rs 1000000')

print(car1.GetInformation())
print()
print(car2.GetInformation())