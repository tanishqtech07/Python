#functions 
#a function is a block of code which only runs when it is called. we can pass data, known as parameters, into a function. a function can return data as a result. in python we can define a function using the def keyword. for example:
#function ek box jesa hota he jab hum es box ka nam lege tab ye run hoga 
#function create karne ke liye def keyword use karte hai jiska full form define hota hai
#like range print input etc these are built in functions in python but we can also create our own functions using def keyword
#agar aaoko apna function create karna hai to hum def keyword use karte hai uske bad function ka nam dete hai aur uske bad parenthesis lagate hai aur uske bad colon lagate hai aur uske bad indentation me code likhte hai jo function ke andar run hoga jab hum function ko call karenge

# def #function ka name = variable name
"""def greet():# aab enter karne ke bad indentation me code likhna hai jo function ke andar run hoga joki 4 space ka hota hai
    print("hello world")#ye code function ke andar run hoga jab hum function ko call karenge
greet() # function call #function ko call karne ke liye function ka name likhte hai aur parenthesis lagate hai

# aap function ko kitne bar bhi call kar sakte hai 
greet()#function call
greet()#function call
greet()#function call
"""
#take users input of name and print name with hello world
"""def greet2():#parameters
    name1=input("enter your name:")
    print(f"hello {name1}")
greet2()#arguments 
"""

#by giving name as parameter and passing name as argument
"""def greet3(name2):#parameters
    print(f"hello {name2}")
greet3("MS Dhoni")#arguments"""

#name ke anxder jo bhi hoga wo print hoga 
"""def greet4(name3):#parameters
    print(f"hello {name3}")
greet4("MS Dhoni")
greet4("Virat Kohli")
greet4("Rohit Sharma")"""

#que print greatest between two no. without using function
"""v1=int(input("enter first number:"))
v2=int(input("enter second number:"))
for i in range(1):
    if v1>v2:
        print(f'{v1} is greater than {v2}')
    elif v2>v1:
        print(f'{v2} is greater than {v1}')
    else:
        print(f'{v1} and {v2} are equal')
    """
#que print greatest between two no. using function
"""def greatest():
    v1=int(input("enter first number:"))
    v2=int(input("enter second number:"))
    for i in range(1):
        if v1>v2:
            print(f'{v1} is greater than {v2}')
        elif v2>v1:
            print(f'{v2} is greater than {v1}')
        else:
            print(f'{v1} and {v2} are equal')
greatest()#function call"""

#que reverseing a string using function and checking whether the string is palindrome or not
'''def reverse_string():
    s=input("enter a string:")
    reverse=s[::-1]
    for i in s:
        reverse=i+reverse
    print(f"the reverse of the string is :{reverse}")
    if s==reverse:
        print(f"{s} is a palindrome string")
    else:
        print(f"{s} is not a palindrome string")
reverse_string()'''

#using prameter and argument
"""def reverse_string2(s1):#parameters
    reverse=s1[::-1]
    if s1==reverse:
        print(f"{s1} is a palindrome string")
    else:
        print(f"{s1} is not a palindrome string")
reverse_string2("taniinat")#arguments
reverse_string2("hello")"""



#adding to two number
'''def add(a,b):
    print(a+b)
add(10,20)'''

#by changing the value 
'''def add(a=10,b=20):
    print(a+b)
add()
add(8)
add(9,10) '''

#multiplication program
'''def mul(a=10,b=2):
    print(a*b)
mul()
mul(5)
mul(5,5)
'''

#printing name 
'''def info(name,age):
    print(name,age)
info("tanishq",19)
info(age=19,name="tanishq")'''

#function with return statement
"""def add():
    a=10
    b=20
    return a+b 
print(add())"""

#parameter and argument

'''def add(a,b):#function define krete waqt parameters dete hai joki variable name hota hai
    print(a+b)
add(10,20)#function call karte waqt arguments 
'''


#type hint add(a,b):#function define karte waqt parameters dete hai joki variable name hota hai aur type hinting karte hai ki a aur b int type ke honge
"""def add(a:int,b:int):
    print(a+b)
add(10,20)
"""
#local and global variable
#local variable is a variable which is defined inside a function and can only be accessed inside that function
#global variable is a variable which is defined outside a function and can be accessed anywhere in the program

"""def add(a,b=0):#default parameter value dena
    print(a+b)
add(10)

def add(a,b=0):#default parameter value dena
    print(a+b)
add(10,50)#a mai 10 jayega aur b mai 50 jayega to output 60 aayega"""

#accept and parameter named as "n" and print the factorial of that number
'''def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i 
        print(f"{n}!={fact}")
factorial(5)
'''

#keyword arguments
"""def info(name,age,gender,address):
    print(name)
    print(age)
    print(gender)
    print(address)
info(name="tanishq",age="19",gender="male",address="bhopal")
    """
    
#check if a number i palindrome or no using keyword arguments without converting it into string
'''def palidrome(n):
   copy=num
   reverse=0
    while num>0:
    last=num%10
    reverse=reverse*10+last
    num=num//10
    if copy==reverse:
       print(f"{copy} is a palindrome number")
    else:
        print(f"{copy} is not a palindrome number")
palidrome(num=1221)'''

#RETURN keyword
'''
def add(a,b):
    return a+b 
x=add(1,3)
print(x)
'''

#printing the square of multiplicaion of both values
'''def mul(a,b):
    return a*b 
x=mul(2,2)
print(x*x)'''

#fatorial using the function 
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        return fact
    print(fact)
factorial(5)
