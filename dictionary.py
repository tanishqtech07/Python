#dictionary is denoted by {} curly brackets 
# dictionary are made up of the key and value pairs 
#the key in the dictionary is be anything as string,int etc 
#you can print thr dictionary values using the keys of the list 
"""d1={'a':10, 'b':20, 'c':30, 'd':40}
print(d1['b'])
d2={1:10, 2:20, 3:30, 4:40}
print(d2[2])


#items assignment as the key e and value 100 by craeting  a new key 
d1['e']=100 
print(d1)

# if you add the key that rae already exixting than the key will over write 
d1['e']=200
print(d1)

# the dictionary is hetroginous and mutalbe both """

# changing the value of the age 
'''info={'name':'rahul','age':21,'marks':50.25 ,'Present':True}
info['age']=25
print(info)
'''

#METHODS IN DICTIONARY 
#1. .values() it give only values of the dictionary 
'''info={'name':'rahul','age':21,'marks':50.25 ,'Present':True}
print(info.values())'''

#2. .keys() it print only keys of the dictionary
'''info={'name':'rahul','age':21,'marks':50.25 ,'Present':True}
print(info.keys())'''


#3. .items() it print the keys and value both
'''info={'name':'rahul','age':21,'marks':50.25 ,'Present':True}
print(info.items())'''

#you can store list in a list ina dictionary 
#4 .pop() it remove the element by index 
'''info={'name':'rahul','age':21,'marks':50.25 ,'Present':True}
info.pop('name')
print(info)'''

# in the dictionary the number of the  keys are its length


# using the for loop 
'''info={'name':'rahul','age':21,'marks':50.25 ,'Present':True}
for i in info:
    print(i,info[i])'''
    
# applying the for loop nly on the values
'''info={'name':'rahul','age':21,'marks':50.25 ,'Present':True}
for i in info.values():
    print(i)'''
    
#5 .get() it prnt the value of key and if is not present in the dictionary than it gives you NONE 
'''d={'a':10,'b':20,'c':30}
print(d.get('d'))'''

# 6. .update(key:value) it update the value of the key it work as like the item assignment 
'''d={'a':100,'b':200,'c':300}
d.update({'c':500})
print(d)
'''
#7 .clear() it remove all the elenment form tghe dictionary 
'''d={'a':100,'b':200,'c':300}
d.clear()
print(d) # it print the {}'''

# del is used to remove the any element , dictionatr, list , comment for your memory


#QUESTIONS 
#making the dictionary by two list by l1 as for the keys and l2 as for the value
'''l1=['a','b','c','d']# the for loop in this is for only the same index 
l2=[10,20,30,40]
d={}
for i in range(len(l1)):
    d[l1[i]]=l2[i]
print(d)'''

#2 you have a list make the indexes as the keys and elements present on those indexes as value
'''l2=[10,20,30,40]
d={}
for i in range(len(l2)):
    d[i]=l2[i]
print(d)

'''
#3 merge 2 dictionary 
'''d1={'a':10,'b':20}
d2={'c':30,'d':40}
for i in d2:
    if i not in d1:
        d1[i]=d2[i]
print(d1)'''

# you can also wirte this code in a line using the update 


#4 frequency  its is a question of lead code
l=[1,1,1,2,2,3,3,6,6,7,6,3,4,1,2]
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
    
print(d)


