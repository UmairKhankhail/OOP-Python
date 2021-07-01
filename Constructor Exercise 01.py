class Example():

    def __init__(self,num):
        self.num=num
#The set_num function will not set the value as we didnt metion the self which means that the variable the variable belongs to the current object.'''
    
    def set_num(self,num):
        num=num
    
    def get_num(self):
        return self.num

def main():
    obj1=Example(10)

    obj1.set_num(15)

    print(obj1.get_num())

if __name__=="__main__":
    main()