class Example():

    def __init__(self,num):
        self.num=num
    
    def set_num(self,num):
        self.num=num
    
    def get_num(self):
        return self.num
    
obj1=Example(10)

obj1.set_num(15)

print(obj1.get_num())

