# printing the star pattern as the right angle triangle 
"""
*
**
***
****
*****
"""
#CODE 
"""row=6
for i in range(1,6):
    print(i*"*")
    """


#same question as we are taking the user input 
"""rows=int(input("enter the number of rows :"))
for i in range(1,rows+1):
    print(i*"*")"""
    
    
# print in reverse order  ( ulta right angle  triangle print karwa rahe he )
"""
*****
****
***
**
*
"""
#CODE 
"""row=int(input("enter the number of the rows:"))
for i in range(row,-1,-1):
    print(i*"*")"""


#printing the number patteern 
"""
1
22
333
4444
55555
"""
"""n=int(input("enter your number:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")#we useend to print number in a single line and we used another print to change the line number wise 
    print()#ye print har number line ke baad line change kare ga """
    
#without using two for loop 
#converting the i value in str
'''n=int(input("enter the number:"))
for i in range(1,n+1):
    print(i*str(i))
'''
'''#reverse me print karte he 
n1=int(input("enter the number:"))
for i in range(n,-1,-1):
    print(i*str(i))'''
    
# print the pairs of element in a list given element. LEET code question 
nums=[3,2,3,2,2,2]
d={}#{3:2,2:4}
for i in nums:#i->3
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
    
# now we create a loop in whinch the value of i ( count of value) aya
for i in d.values():
    if i%2!=0:
        print('not making pair :')
        break 
else:
    print("making pair ")