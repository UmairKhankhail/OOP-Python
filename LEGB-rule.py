y=4   #-----> Global scope 

def fun1():
  
    z=5  #-----------> Enclosing scope
    def fun2():
        x=9 #-------->local scope
        
        #In order to update enclose variable inside local variable, we use keyword nonlocal
        
        nonlocal z
        z=z+1
        
        print("X : ",x)
        print('inside the function y: ',y)
    fun2()
    print('z: ',z)

fun1()

#Output: 9  4 5