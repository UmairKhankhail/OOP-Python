class Customer():

    def __init__(self):
        customer_id=100

obj=Customer()
print(obj.customer_id)

#This will give us error because self is not mention in the init function so the program is unable to understand that the customer_id belong to which
#object? Hence it will throw an error
