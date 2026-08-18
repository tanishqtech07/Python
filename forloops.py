#loops are use d to perform a task repeatedly until a certain condition is met. There are two main types of loops in Python: for loops and while loops.
#for loops are used to iterate over a sequence (such as a list, tuple, or string) or other iterable object. The syntax for a for loop is as follows:
#while loops are used to execute a block of code as long as a certain condition is true. The syntax for a while loop is as follows:
#for loops works on the total number of iterations, while loops works on the condition. For example, if you want to print the numbers from 1 to 10 using a for loop, you can do it like this:
#range() is a built-in function in Python that generates a sequence of numbers. It takes three arguments: start, stop, and step. The start argument is the number at which the sequence starts, the stop argument is the number at which the sequence ends (not inclusive), and the step argument is the difference between each number in the sequence. If the step argument is not provided, it defaults to 1.
#for loop example
"""a = range(1,101,1) #(start, stop, step)
for i in a:
    print(i)

b=range(50,121)
for i in b:
    print(i)
    
for i in range(-10,31):
    print(i)
for i in range(10,-21,-1):#(10, -21, -1) means start from 10, stop at -21 (not inclusive), and step by -1 (decrement by 1)
    print(i)

for i in range(7,71,7):
    print(i)"""
    
"""c=int(input("Enter a number: "))
for i in range(c,c*10+1,c):
    print(i)"""
"""
for i in range(0,21,2):#printing all even numbers from 0 to 20
    print(i)
for i in range(1,21,2):#printing all odd numbers from 1 to 20
    print(i)"""
    
#break , continue and else in loops 
#break statement is used to exit a loop prematurely when a certain condition is met. When the break statement is executed, the loop is immediately terminated and the program continues with the next statement after the loop.

"""for i in range(1,11):
    if i==3:
        break
    print(i*10)
    
for i in range(1,100):
    if i==50:
        break
    print(i)
    
#continue statement is used to skip the current iteration of a loop and move on to the next iteration. When the continue statement is executed, the rest of the code inside the loop for that iteration is skipped, and the loop continues with the next iteration.

for i in range(1,11):
    if i==3:
        continue
    print(i*10)

for i in range(1,11):
    if i==3 or i==5:
        continue
    print(i*10)
    
#else statement in loops is used to specify a block of code that will be executed when the loop has completed all iterations without encountering a break statement. The else block will be executed only if the loop completes normally, without any interruptions.

for i in range(1,11):
    if i==20:
        break
    print(i*10)
else:
    print("Loop completed normally.")
    
for i in range(1,11):
    if i==5:
        break
    print(i*10)
else:
    print("Loop completed normally.")"""

#break will run than else block will not run and if break is not run than else block will run. In the above example, since the loop completes normally without encountering a break statement, the else block will be executed and "Loop completed normally." will be printed.

"""n=int(input("Enter a number: "))#printing the hello world n times 
for i in range(n):
    print("hello world")
    
nat=int(input("enter a number")) #printing natural numbers from 1 to n
for i in range(1,nat+1):
    print(i)
    
rev=int(input("enter a number")) #printing the reverse of a number
for i in range(rev,0,-1):
    print(i)

mul=int(input("enter a number")) #printing the multiplication table of a number
for i in range(1,11):
    print(f"{mul} x {i} = {mul*i}")"""
    
"""ns=int(input("enter a number")) #printing the sum of first n natural numbers
sum=0
for i in range(1,ns+1):
    sum=sum+i
print(sum)"""

"""fc=int(input("enter a number:")) #printing the factorial of a number
fact=1
for i in range(1,fc+1):
    fact = fact *i
print(fact)"""

#TANISHQ BHAIYA QAUSTIONS
#qustion: Write a program to count the total even and odd numbers from 1 to n.
count=int(input("enter a number:"))#counting the total even and odd numbers from 1 to n
even=0
odd=0
for i in range(1,count+1):
    if i%2==0:
        print(f"{i} is an even number")
        even+=1#even=even+1 #shorthand operator for adding 1 to the variable even
    else:
        print(f"{i} is an odd number")
        odd+=1#odd=odd+1

print("the total even number are :",even)
print("the total odd number are :",odd)

#question2 : count the total number of vowels and consonants in a string.
"""s="hello sherry"
count=0
consonants=0
for i in s:
    if i in "AEIOUaeiou":
        count=count+1
    else:
        consonants=consonants+1
        
print(f"count of vowels are :{count}")
print(f"count of consonants:{consonants}")
"""
#question3 : print 
"""num=int(input("enter the number:"))
for i in range(2,num):
    if num%i==0:
        print(f"this is not aprime number {i}")"""
        
        
#1. Agar kisi number ke factors 2 ya 2 se kam hai toh prime
# for i in range(1,51):
#     factors = 0
    
#     for j in range() 2,num//2

#question4 : print the factorial of a number
"""num=10
for i in range(1,num+1):
    if num%i==0:
        print(i)"""
#question5 : count the total number of factors of a number
"""num=10
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
print(count)"""
#printing the number of digits in a number
"""num=int(input("enter a number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        print(i)
        count+=1
        
        
if count==2:
    print(f"{count} is a prime number")
else:
    print(f"{count} is not a prime number")"""
#printing the factors of a number and their sum
"""n1=int(input("enter a number:"))
sum=0
for i in range(1,n1+1):
    if n1%i==0:
        print(i)
        sum+=i
print(f"Sum of factors: {sum}")
"""

#question print the prime numbers from 1 to n
"""n2=int(input("enter a number:"))
for i in range(2,n2+1):
    if i>1:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i)"""

#seprate each digit of a number and print it on a new line
"""num4=int(input("enter a number:"))
num=str(num4)
for i in num:
    print(i)
    """

    
