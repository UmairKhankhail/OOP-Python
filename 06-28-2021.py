class Humans():

    def SetName(self,name):
        self.Name=name

    def SetAge(self,age):
        self.Age=int(age)

    def SetGender(self,gender):
        self.Gender=gender
    def GetInformation(self):
        return "Name: "+self.Name+"\nAge: "+str(self.Age)+"\nGender: "+self.Gender

man1=Humans()

man1.SetName('Farooq Khan')
man1.SetAge(18)
man1.SetGender('Male')

man2=Humans()
man2.SetName('Sahar Bano')
man2.SetAge(20)
man2.SetGender('Female')

print(man1.GetInformation())
print()
print(man2.GetInformation())
