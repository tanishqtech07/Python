#sets ko "{ }" se define karte hai 
# set does not allows the duplicatev value 
# sets are a data types in which the indexing it not allowed 
#set is a hetrogenous data type nut it not alloes the boolean vakues 
#the sets are mutable 
# in the set item assignment is not  allowed but th item adding are allowed 
'''s={}#empty set 
print(type(s))# it not print the data type set it print dictionary
#this is impicity canversion '''

'''s1=set()
print(type(s1))#it print the data type as the set by explicit conversion 
'''
'''s2={1,2,3,4,5}
print(s2)
print(type(s2))
'''

'''s={'hello',1,3.14,True}
print(s)
'''

#methods in set

#1. adding new element in set 
#items addintg 

# 1. .add() are used

'''s={1,1,1,2,2,3,3,4,4,5,5,}
s.add(100)
print(s)'''


# adding multiple value in a set
# 2. .update()
'''s={1,1,1,2,2,3,3,4,4,5,5,}
s.update([200,300,400,500])
print(s)'''

# 3. .remove()
#remove the elemnets from the set
'''s={1,1,1,2,2,3,3,4,4,5,5,}
s.remove(1)
print(s)
'''

#if the elemwnt are not in the set and you are removing that type of the value then it give the error BUT  IF YOU USE THE .discard() the error will not shows
'''s={1,1,1,2,2,3,3,4,4,5,5,}
s.discard(6)
print(s)'''


#remove all elemnet and printing. empty set()
'''s={1,1,1,2,2,3,3,4,4,5,5,}
s.clear()
print(s)'''

#advansed methods in the sets
"""
1. union- sare elemnts between your set 
2. intersection - dono sets ke beech mai jo common values """
    
'''s1={1,2,3,4,5}
s2={1,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))'''


# 3 . difference matalb ek set mai present ho par dusre mai nhi like s1 me ho par s2 mai na ho 
# diffenerne()

'''s3={1,2,3,4,5}
s4={1,2,6,7,8}
print(f"difference of set1 and set2 {s3.difference(s4)}")
print(f"difference of set1 and set2 {s4.difference(s3)}")
'''
# 4.symmetric difference print the element that are not common ( common ko chhod kar jo bach rahe he wo values dega )
# denoted by symmetric_difference
'''print(f"symmetric difference of set1 and set2 {s3.symmetric_difference(s4)}")
print(f"symmetric difference of set1 and set2 {s4.symmetric_difference(s3)}")
'''


l=[1,2,1,2,1,3,3,3,4,5,6,7]
s=set()#set # use samll barckets 
for i in l:
    s.add(i) 
print(s)


