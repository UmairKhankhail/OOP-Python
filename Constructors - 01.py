#The memory of any object depends upon its constructor. The constructor will decide that how much memory it is going
#to take in the heap memory(memory for object or instrance variables.)

#The init method or constructor runs as we create an instance of any class, if we don't declare it, it is created explicitly

class Mobile():
    
    def __init__(self):
        print("Constructor runs")

m1=Mobile()