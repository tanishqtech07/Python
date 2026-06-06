#chapter 5 = input and output
age1 = 24 
name1 = 'harsh' 
# 1st way of variables and printing them
print("hello your name is ",name1,"and your age is ",age1)  #this is one way to print the name and age

#using of formated string 
#f string is a way to format the string in a better way and it is more readable and easier to use
print(f"hello your name is {name1} and your age is {age1}") #this
#is another way to print1 the name and age using f string

#$ input and output function 
#waht is prompt ? prompt is the message that is displayed to the user when the input function is called it is used to ask the user for input

age2=input("enter your age  : ")
print(f'your age is {age2}') #this will print the age that the user has entered
age2=int(age2) #this will convert the age to int in line 17
print(f'your age after 6 years will be {age2 + 6}') #this will print the age after 6 years by converting the age to int and adding 6 to it
# we get error in age becouse python considers the input as a string and we cannot add an integer to a string so we have to convert the age to int before adding 6 to it
#age2=int(age2) #this will convert the age to int in line 17


#direct input by data types 
age3=int(input("enter your age  : ")) #this will convert the age to int in line 20
print(f'your age is {age3}') #this will print the age that the user has entered
print(f'your age after 6 years will be {age3 + 6}') #this will print the age after 6 years by converting the age to int and adding

name2 = input("enter your name : ") #this will take the name as input from the user and store it in the variable name
print(f'your name is {name2}') #this will print the name that the user has entered




