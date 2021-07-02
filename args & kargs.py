# *args
# If we write (*) *args before any variable, then it is passed as tuple

# If we write double (**) **kwags before any variable, then it means that it is passed as a dictionary

class Human():

    def __init__(self,*tuple):
        #Now I don't want to pass all the parameters in init functions, so I will pass a tuple into it (starting with a * ) 
        
        self.Name=tuple[0]
        self.Age=tuple[1]
        self.Education=tuple[2]

    def GetName(self):
        return self.Name

    def GetAge(self):
        return self.Age

    def GetEducation(self):
        return self.Education

man1=Human('umair khan',19,'undergraducate')
print(man1.Name) 
print(man1.GetEducation())
print(man1.GetAge())

#Now what if change the order of data while passing the tuple... Since I am storing tuple[0] in self.Name but then it may store any other value and when I call GetName function it may return uncorrect value to me.
# In these case the concept of **kwargs comes into play.

class Car():
    
    def __init__(self,**dictionary):
        self.data=dictionary

    def GetType(self):
        return self.data['Type']

    def GetModel(self):
        return self.data['Model']
    
    def GetPrice(self):
        return self.data['Price']
def main():
    car1=Car(Type="motorcycle",Model=2003,Price=100000)
    print(car1.GetModel())

if __name__=="__main()__":
    main()