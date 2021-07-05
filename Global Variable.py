y=10
def function():
     
     #It will give error because we can not modify global variables inside the local scope
     y=y+1
     print('Varible inside the funciton: ',y)

#first it will run print funciton.
print(y)
#then error, therefore commented this
#function()


# Now if we want to change the global variable (for local use) inside the scope of local variable, we use global keyword.

x=50

def function1():
    
    global x
    
    x=x+1

    print("Value of X incremented for the funciton i.e. ",x)


print("modified value: ",x)
function1()

#if we write it before the function, then the value will not be modified 

print("modified value: ",x)