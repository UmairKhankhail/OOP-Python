#Instance Variables
#Class/Static Variables (Class varaibles are also called static varaibles.)

class Car():
    
    #Class variables
    body='Metal'

    def __init__(self):
        self.Type="BMW"
        self.Mileage=2000

car1=Car()
car2=Car()

#Now If I call the variables for both the objects, this will give us same output
#These variables belongs to objects because it depends upon objects, These can not be accessed through class name.

#print(Car.Type)   -----> It is commented because with this the code won't run.

print(car1.Type,car1.Mileage)
print(car2.Type,car2.Mileage)

#But if I want to change the type and mileage just for car1, It will be changed while the variables will remain same for car2

car2.body="Water"
car1.Type='Carolla'
car1.Mileage=50000

print(car1.Type,car1.Mileage)
print(car2.Type,car2.Mileage)

#Now if all the objects of the class have some simillar properties or fixed properties for all objects, I will use class variables for that because that belongs to class.
#These variables can be accessed through both class and objects.#  
# #class varaibles can also be changed

print(Car.body)
print(car2.body)

car2.body="Water"
print(Car.body)
print(car2.body)