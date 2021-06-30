class Humans():

    def __init__(self,name,age,height,education):
        self.Name=name
        self.Age=age
        self.Height=height
        self.Education=education

    def GetInformation(self):
        return 'Name: '+self.Name+' Age: '+str(self.Age)+' Height: '+str(self.Height)+' Education: '+self.Education

def main():

    human1=Humans('Umair Khan',19,6.1,'Undergraducate')
    human2=Humans('Kamran Bangash',33,6.0,'Masters')

    print(human1.GetInformation())
    print()
    print(human2.GetInformation())

if __name__=="__main__":
    main()    