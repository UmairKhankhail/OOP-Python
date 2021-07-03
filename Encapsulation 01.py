class Car():

    def __init__(self,type,model,price,color):
        
        #I want to make my all these variables private

        self.__Type=type
        self.__Model=model
        self.__Price=price
        self.__Color=color

    #I can also make my functions private
    #setter function
    def __set_type(self,value):
        self.__Type=value

    def set_model(self,value):
        self.__Model=value

    def set_Color(self,value):
        self.__Color=value

    def set_price(self,value):
        self.__Price=value

    def __get_price(self):
        return self.__Price
    
    def get_type(self):
        return self.__Type

    def get_color(self):
        return self.__Color
    
    def public_method_for_private_method(self):
       return self.__get_price()

car1=Car('Alto',2009,10000000,'Black')

print(car1.get_color())
car1.set_Color('red')

#private methods of the class can neither be accessed outside the class nor by any base class. However, private methods can be accessed by calling the private methods via public methods.

#car1.__set_price(40000)


#print(car1.get_price())


#print(car1.get_color())

print(car1.public_method_for_private_method())