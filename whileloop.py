#while loop 
#while is a keyword in python which is used to create a while loop. A while loop is a control flow statement that allows code to be executed repeatedly based on a given boolean condition. The syntax of a while loop is as follows:
#in python while loop is used to execute a block of code repeatedly as long as a given condition is true. The syntax of a while loop is as follows:
#while condition:
    #code to be executed
#the condition is evaluated before the execution of the loop body. If the condition is true, the code inside the loop is executed. After the code inside the loop is executed, the condition is

#we have to make while condition false at same point oterwise it will become infinite loop and it will run forever. For example, if we want to print the numbers from 0 to 10 using a while loop, we can do it like this:
"""i=0 #print number from 0 to 10 using while loop
while i<11:
    print(i
    i+=1 #this is the increment operator which is used to increment the value of i by 1 in each iteration of the loop
    #i+=1 is equivalent to i=i+1"""
#print number from 0 to 10 using while loop 
"""i=0
while i<11:
    if i==5:
        break #this is the break statement which is used to exit the loop when the condition is met
    print(i)
    i+=1"""
    
#questions print the last digit of a number
"""num1=1025
print(1054%10)
print(105%10)
print(10%10)
print(1%10)"""
#using the while loops for printing the last digit of value
"""num2=1054
while num2>0:
    print(num2%10)
    num2=num2//10 """#this is the floor division operator which is used to divide the number by 10 and get the quotient as an integer. This is used to remove the last

#printing the sum of al values also with the valuer
'''num2=1054
sum=0
while num2>0:
    last=num2%10
    print(last)
    num2=num2//10
    sum=sum+last
print("the sum is :",sum)'''


#.  '''  VERY VERY IMPORTANT QUESTION  '''
#you have to cheak a number is palindrome or not using while loop
#the palindrome number is a number which is same when read from left to right and right to left. For example, 121 is a palindrome number because it is same when read from left to right and right to left. But 123 is not a palindrome number because it is not same when read from left to right and right to left.
#we have to make two variables one is for storing the original number and another is for storing the reverse of the number. Then we have to compare both the variables if they are same then the number is palindrome otherwise it is not a palindrome.
#we added reverse variable uper of while loop because if we store it in while lop reminder will be 0 agian and again and it will become infinite loop. For example, if we want to check whether 1221 is a palindrome number or not, we can do it like this:
"""num=1221
copy=num
reverse=
while num>0:
    last=num%10
    reverse=reverse*10+last
    num=num//10
if copy==reverse:
    print(f"{copy} is a palindrome number")
else:
    print(f"{copy} is not a palindrome number")"""



#by taking user input
"""num=int(input("enter a number: "))
copy=num
reverse=0
while num>0:
    last=num%10
    reverse=reverse*10+last
    num=num//10
if copy==reverse:
    print(f"{copy} is a palindrome number")
else:
    print(f"{copy} is not a palindrome number")"""


#STRING QUESTIONS
#print a stroing in reverse order
"""name='Mohit'
print(name[::-1])
print(len(name))
print(name.upper())
print(name.lower())
name2=name
print(name2)"""

#print(lower case letter + uppercase letter) lower case of a string first that upper case letters and it is called string concatenation 
"""st1="PyThon"
lower=""
upper=""
for i in st1:
    if i.islower():
        lower=lower+i
    else:
        upper=upper+i
print(lower+upper)
"""
#taking user input and doing the same thing
"""st2=input("enter a string: ")
lower=""
upper=""
for i in st2:
    if i.islower():
        lower=lower+i   
    else:
        upper=upper+i
print(lower+upper)"""

#question
#Count all letters, digits, and special symbols from a given string
    # Given: str1 = "P@#yn26at^&i5ve"
    # Expected Outcome:
    # Total counts of chars, digits, and symbols
    # Chars = 8
    # Digits = 3
   # Symbol = 4

"""st3="P@#yn26at^&i5ve"
char=0
digit=0
symbol=0
for i in st3:
    if i.isalpha():
        char=char+1
        print("char=",i)
    elif i.isdigit():
        digit=digit+1
        print("digit=",i)
    else:
        print("symbol=",i)
        symbol=symbol+1
    

print(f"chars={char}")
print(f"digits={digit}")
print(f"symbol={symbol}")"""
#taking user input and doing the same thing
"""st4=input("enter a string: ")
char=0
digit=0
symbol=0
for i in st4:
    if i.isalpha():
        char=char+1
        print("char=",i)
    elif i.isdigit():
        digit=digit+1
        print("digit=",i)
    else:
        print("symbol=",i)
        symbol=symbol+1
    

print(f"chars={char}")
print(f"digits={digit}")
print(f"symbol={symbol}")"""
#cpmare two strings and print the common characters in both the strings
'''st5=input("enter a string: ")
st6=input("enter a string: ")
common=""
for i in st5:
    if i in st6:
        common=common+i
        print(f"{i} is common in both the strings")
        print("common=",True)
        
    else:
        print(f"{i} is not common in both the strings")
        print("common=",False)
'''

#qusetion:  Count Vowels from given string
"""st7=input('enter the string:')
vowel=0
for i in st7:
    if i in "AEIOUaeiou":
        print(i)
        vowel=vowel+1
print(vowel)"""

#Reverse a string
'''st8=input("enter string:")
for i in st8:
    
    print(st8[-1::-1])'''
    
#question Check string is Pallindrome or not**
st9=input("enter the string")








