def add():
    num1 =int(input("enter number 1 : "))  
    num2 =int(input("enter number 2 : ")) 
    print("sum 2 numbers =",num1+num2)
 
def sub():
    num1 =int(input("enter number 1 : "))  
    num2 =int(input("enter number 2 : "))  
    print("sum 2 numbers =",num1-num2)    
    
def mul():
    num1 =int(input("enter number 1 : "))  
    num2 =int(input("enter number 2 : "))  
    print("sum 2 numbers =",num1*num2)
 
 
while(1):
    n=int(input("1. add\n2. sub\n3. mul"))
    
    if(n==1):
        print("you have selected add")
        add()
        
    elif(n==2):
        print("you have selected sub")
        sub()
        
    elif(n==3):
        print("you have selected mul")
        mul()
    else:
        print("wrong input")