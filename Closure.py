
# The technique to call a function outside of its scope is called Closure.

#Criteria: 1. We must have a nested funciton.
#          2. Nested function must refer values in enclosing scope.
#          3. Nested funciton must return the enclosing funciton.


def enclose():
    
    x=10
    
    print('This is enclose function.')


    def nested():
        
        nonlocal x
        print('This is local function.')
        x=x+100
        
        return x
    return nested
    
a=enclose()

print(a())