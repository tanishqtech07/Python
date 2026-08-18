# recursion is a programming technique where a function calls itself in order to solve a problem. It typically involves a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.
# printing number from 1 to 10 usind recursion
"""def display(num):
    if num>10:
        return#return statement is used to exit the function when the base case is reached. It prevents further recursive calls and allows the function to unwind back to the previous calls.
    print(num)
    display(num+1)
display(1)
"""
#printing n natural numbers using recursion
"""def display(n):
    if n==0:
        return
    display(n-1)
    print(n)
display(100) 
"""


#printing number from 10 to 1 using recursion
'''def display(num):
    if num<1:
        return
    print(num)
    display(num-1)
display(10)
'''
#printing the factorial of a number using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
        
print(factorial(5))

#lambda function
#args 
#kwargs 
# they three are skiped 