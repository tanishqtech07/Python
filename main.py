print("hello p24")
#chapter 1 to 4 


#1.chapter 1 Comments and variables
# (# This is a comment)
# ("""This is a comment""") for multiple lines

#variables

hello=25
a=12
p24=56
#you can not start a variable with a number like 24p is worong
#you can not use space in variable name like p 24 is wrong
#you can not use special characters in variable name like p@24 is wrong (@$%^&*() are special characters


#pascal case ; capitalise the first letter of each word and no space in between (PascalCase)
HelloBrother= 22

#camel case ; capitalise the first letter of each word except the first word and no space in between (camelCase)
helloBrother= 24

#snake case ; all letters are small and words are separated by underscore (snake_case)
hello_brother_how_are_you= 34


# chapter 2 Data types 

#number data type: int.   ,    float.   ,    complex.
a= 25 #int a is capturing the value 25
b=-13 #int b is capturing the value -13
print(type(a)) #this will print the data type of a which is int
print(type(b)) #this will print the data type of b which is int



c=44.55 #float c is capturing the value 44.55
d=-0.56 #float d is capturing the value -0.56
e=10/5 #float e is capturing the value 10 divided by 5 which is 2.0
print(type(c)) #this will print the data type of c which is float
print(type(d)) #this will print the data type of d which is float
print(type(e)) #this will print the data type of e which is float


#complex data type shows iota denoted by j
f= 2+3j #complex f is capturing the value 2 plus 3
print(type(f)) #this will print the data type of f which is complex


#string data type : in  string yo wirte anything in it quotes like " " or ' ' or """ """ or ''' '''
s1='hello how are you'
s2="hello how are you"
s3='''hello how are you'''

s4='he said to me  "hello how are you"'
print(type(s1)) 



#boolean data type : it can only have two values True or False you have to write them with capital T and capital F
b1= True
b2= False
print(type(b1)) #this will print the data type of b1 which is bool
print(type(b2)) #this will print the data type of b2 which is bool


#chapter 4 strings 

st1="harsh"
#ord function gives the unicode value of a character
print(ord("A"))
print(ord("a"))
print(ord("1"))
#in python every character has a unicode value and the ord function gives the unicode value of a character like cahracter A, a number emoji everything

#INDEXING  always starts with 0 in python
print(st1[0])
print(st1[1])
print(st1[2])
print(st1[3])
print(st1[4])

#negative indexing starts with -1
print(st1[-1])

print(st1[1],st1[-4])


#slicing [start:stop:step]
#start is the index from where you want to start slicing
#stop is the index where you want to stop slicing but it will not include the stop index 
#in stop index you have to write index +1
#step is the number of characters you want to skip while slicing
print(st1[2:5:1])#printing rsh from harsh

st2="shreyians"
print(st2[0:4:1])
print(st2[0:9:2])#printing sryas from shreyians

#fdefault value of start is 0
print(st2[::])#[0;last index:1] this will print the whole string
print(st2[5::1])#ians


#TYPE CONVERSION int() float() str() bool()
tp=23.56
tp1=int(tp) #this will convert the float value 23.56 to int value 23
print(tp1)
print(type(tp1)) #this will print the data type of tp1 which is int


#in python you can re assign a variable to a different data type and value

tp2=12
tp2=40
print(tp2) #this will print the value of tp2 which is 40
tp2=tp2+10.45
print(tp2) #this will print the value of tp2 which is 50

tp2= int(tp2) #this will convert the float value 50.45 to int value 50
print(tp2) #this will print the value of tp2 which is 50

#you connot convert a string to int if the string is not a number like "hello" or "23.56" but you can convert a string to int if the string is a number like "23" or "56"
#tp3="hello" #this will give an error because "hello" is not a number

#tp3="23.56" #this will give an error because "23.56" is not a number because pyrhon understands . as strings character and not as a decimal point 
# but you can convert a string to float if the string is a number like "23.56" or "56.78"

tp3="23"
tp3=int(tp3) #this will convert the string value "23" to int value 23
print(tp3) #this will print the value of tp3 which is 23
print(type(tp3)) #this will print the data type of tp3 which is int


tp4="23.56"
tp4=float(tp4) #this will convert the string value "23.56" to
print(tp4) #this will print the value of tp4 which is 23.56
print(type(tp4)) #this will print the data type of tp4 which is float

#using str you can convert any data type to string
tp5= True
tp5=str(tp5) #this will convert the boolean value True to int value 1
print(tp5) #this will print the value of tp5 which is True

#in bool all values are true except 0, 0.0, empty string "" and False [] {} () None

print(bool(0))
print(bool(12))
print(bool(-12))
print(bool(0.0))
print(bool(-0.56))
print(bool(""))
print(bool("hello"))
print(bool(12.56))
print(bool([]))
print(bool('0'))

#two types of type conversion implicit and explicit
#implicit type conversion is when python automatically converts one data type to another data type without you having

tp6=12
print(tp6/2)
print(type(tp6/2))
#in the above code python automatically converts the int value 12 to float value 12.0 and the result of 12.0 divided by 2 is 6.0 which is a float value

#explicit type conversion is when you manually convert one data type to another data type using the type conversion functions like int() float() str() bool()
tp7=12
tp7=float(tp7) #this will convert the int value 12 to float value 12.0
print(tp7) #this will print the value of tp7 which is 12.0
print(type(tp7)) #this will print the data type of tp7

