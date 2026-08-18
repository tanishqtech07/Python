name=input("enter your name ")
age=int(input("enter your age "))
if age>=18 :
    print(f"hello {name} you are a vaild voter ")
if age<=18 :
    print(f"hello {name}you are a valid voter after {18-age} :")
else:
    print(f"hello {name} you are not a vaild voter ")
    
    
year = int(input("tell your year :-"))
if year%100==0 and year%400==0:
    print("leap year")
elif year%100==0 and year%4 :
    print("leap year")
else:
    print("not a leap year")
    
    
temp=float(input("tell your temperature:"))
if temp>=-5 and temp<=10:
    print("freezing cold")
elif temp>=11 and temp<=25:
    print("pleasent")
elif temp>=26 and temp<=40:
    print('hot')
elif temp>=41 and temp<=60:
    print("very hot")
else:
    print("very hot tempearture :")
    
a= int(input('enter the 1st integer:'))
b= int(input('enter the 2nd integer:'))
c= int(input('enter the 3rd integer:'))
if a==b and b==c:
    print("all are equal")
elif a==b or b==c or a==c:
    print("any two are equal")
else:
    print("none are equal")
    
char = input("give me an alphabet:")
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='n':
    print("the char are vowel")
else:
    print('these are consonent')
    



    
