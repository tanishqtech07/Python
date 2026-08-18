'''we can perform opeartion with a file 
1.read() -> r mode {kisi bhi file ko sirf read kata hai }
2.a-> kisi bhi existing content  ke last me new content add karta hai
3.w(write)-> kisi bhi existing file me content add karta he (or agar file me peh;le se contant exist karta he file me to new contant se replace kar dega OR agar file exist nahi karti he to new file create kar dega  
4.x-> create a file '''


#reading a file 
file=open('function.py','r')
print(file.read())
file.close()

#using 'w' mode (writing mode)
file=open('superman.txt','w')
file.write('this is hanuman file ')
file.close()
 
#using 'a' mode (append mode)
file=open('superman.txt','a')
file.write("this content will added at the last")
file.close()

#with keyword {aap file open karoge to file apne aap close wo jay gi}
with open('superman.txt','r') as file:
    print(file.read())

with open('hanuman.txt','w') as file:
    file.write("this is siyaram file")
    

#deleting data from a file 
import os #operating system
os.remove('superman.txt')