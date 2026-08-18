"""data structure ( advanced data types)
#1.lists
#2.dictionaries
#3.tuples
#4.sets """

#list: list is denoted by [] square brackets and it is mutable data type
#list=[] this is an empty list
'''l=[10,20,30,40,50]
print(l)
print(type(l))'''

#in list you can store different data types like int, float, string, boolean, list, tuple, set, dictionary

# 1. hetrogeneous list (hetrogeneous data structure)-multiple data types can be stored in a single list and duplicates are allowed
'''l1=[7,"tanishq",True,3.14]
print(l1)
print(type(l1))
'''
'''l2=[10,20,30,40,50]
print(l2[3]) #accessing the 4th element of the list

#changing the value of the list or assigning a new value to the list
l2[3]=700
print(l2)#this is know as item assignment in list'''

#mutable ; means mai list mese kisi bhi value ko change kar sakta hu , add kar sakta hu , remove kar sakta hu , replace kar sakta hu 
#list mai wo index use mat karna jo exist nahi karta

'''l3=[10,20,30,40,50]#item wise looping
for i in l3:
    print(i)'''
    
#index wise looping
'''l4=[10,20,30,40,50]
for i in range(len(1)):#i->0,1,2,3,4
    print(i,1[i])'''
    
#questions
#printing the number greater than 15
"""l5=[1,67,10,25,14,77]
for i in l5:
    if i>15:
        print(i)"""
        
#print the index of the number that number are greater than 15 
'''l6=[1,67,10,25,14,77]
for i in range(len(l6)):
    if l6[i]>15:
        print(i)'''


#sum all the elements of list
'''l7=[10,20,30,40,50]
sum=0
for i in l7:
    sum=sum+i 
    print(i)
print(sum)'''

#slicing 
#we know that in slicing their is start stop step
'''l8=[10,20,30,40,50]
print(l8[1:4:1])
'''

#method in list
#jiske aage . dot lag jay wo method hoti hai 

#1, .append 
# append method is used to insert  new element in last but append insert only one element in one time  
'''l9=[10,20,30,40,50]
l9.append(100)
print(l9)'''


#2 .extend()

'''l10=[10,20,30,40,50]
l11=[60,70,80]
l10.extend(l11)
print(l10)
'''
#3 .insert(index,value) insert is used to add element with a specific idex 
'''l12=[10,20,30,40,50]
l12.insert(1,100)
print(l12)'''

#4 .pop() pop is used to remove the element by indexing 
'''l13=[10,20,30,40,50]
l13.pop(1)
print(l13)'''

#5 .remove() remove is used to remove the element in a list 
# if in a list  their is a duplicate is present so it remove the first element of duplicate 
'''l14=[1,2,3,45,5,6,9,74,34,24]
l14.remove(45)
print(l14)'''

#6. len() len is a function that is uesd to find the length of the list 
'''l16=[1,5,5,5,5,2,3,4,5]
print(len(l16))
'''
#questions :
#38) Accept List elements and reprint it
'''n=int(input("enter the size of the list :"))
l=[]
for i in range(n):
    element=input("enter the elemnet of list :")
    l.append(element)
print(l)'''
# the list print in string element if you can add the specific data type than. it print the data type 

#39) Print  List elements in reverse order
'''n=int(input("enter the size of the list :"))
l=[]
for i in range(n):
    element=int(input(f"enter the elemnet {i} of list :"))
    l.append(element)
print(l)
print(l[::-1])'''
# by for loop 
'''n=int(input("enter the size of the list :"))
l=[]
for i in range(n):
    element=int(input(f"enter the elemnet {i} of list :"))
    l.append(element)
print(l)
for i in range(len(l)-1,-1,-1):
    rev_l=[]
    print(l[i])# if you give i than it will print index in reverse order
    l.append(rev_l)
print(rev_l)'''
    
# 40) Print positive and negative elements of an List
'''l=[10,-9,20,30,-12,-15]
neg=[]
pos=[]
for i in l:
    print(i)
    if i<0:
        neg.append(i)
   else:
        pos.append(i)
print(neg)
print(pos)
'''

# 41) Print list in ascending or descending order
#bubble sort questions 
'''l=[1,5,3,7,4,10]
for i in range(len(l)):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
print(l)'''

#printing hello world five times
'''a=("hello world"*5)
print(a)'''

#42) Accept size n from user and create a n size List then take n inputs into the and finally Print the sum of all elements in the List in the following manner
# 10 + 20 + 30 = 60
'''n=int(input("enter the size of list :"))
l=[]
for i in range(n):
    element=int(input(f"enter the element {i} of list "))
    l.append(element)
print(l)
sum=0
for j in range(len(l)):
    sum=sum+j
print(j)
    '''
    
#Paillndrome or not.
#Method - 1
'''l = [1,2,2,1]
rev_l = []

for i in range(len(l)-1,-1,-1):
    rev_l.append(l[i])

if l == rev_l:
    print('List is Paillndrom..')
else:
    print('List is not Paillndrome..')

'''

#Method - 2
'''l = [1,2,2,1]
for i in range(len(l)): #i->0
    if l[i] == l[len(l)-1-i]: #l[0] != l[3] -> 1 != 1
        print('Not Paillndrome') #Print
        break
else:
    print('List is Paillndrome')

'''



#Enumerate -> List -> [10,20,30,40,50] -> Index -> 0,1,2,3,4
#Enumerate -> index ke sathn unki values bhi dega.
'''l = [10,20,30,40,50]
for index, value in enumerate(l):
    print(index, value)

for index, value in enumerate(l):
    print(index+1, value)
l = [1,2,3,4,5]
l2 = [1,3,4,5,6]
new = [] #common elemets rakhne hai.'''


n = int(input("enter the numebr of elements you want to add in the list :"))
l=[]
large=0
second_large=0
for i in range(1,n+1):
    element=int(input('enter the elemnts :'))
    l.append(element)

for j in l:
    if j>large:
        large=j
l.remove(large)
for s in l:
    if s>second_large:
        second_large=s
print(second_large)
        


    