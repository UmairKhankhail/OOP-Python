class Car():
    
    def __init__(self,type,model,price,miles):
        self.Type=type
        self.Model=model
        self.Price=price
        self.Miles=miles
    
    def GetInformation(self):
        return "Type: \n"+self.Type+"Model: \n"+str(self.Model)+"Price: \n"+str(self.Price)+"Miles: \n"+str(self.Miles)
def main():
    car1=Car("BMW",2000,100000,500)
    print(car1.GetInformation())
    print()
    car2=Car('Carolla',1999,2000000,1000)
    print(car2.GetInformation())

if __name__=="__main__":
    main()