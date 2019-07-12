#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
str1='email Id : call.del@airindia.in'
match=re.search(r'[a-zA-Z ]+:([a-zA-Z ]+\.[a-z]+@([a-z]+)\.[a-z]+)',str1)
print(match)
print(match.group(0))
print(match.group(1))
print(match.group(2))


# In[4]:



for _ in range(int(input())):
    line = input()
    
    while ' && ' in line or ' || ' in line:
        line = line.replace(" && ", " and ").replace(" || ", " or ")
    
    print(line)
    


# In[ ]:


import re
str1='email Id : call.del@airindia.in'
match=re.serach(r'\S+@\S+)


# In[2]:


import re
str1='Landline Number : 011-24667473'
str2='Landline Number : 011.24667473'
str3='Landline Number : 011*24667473'
match=re.search(r'[a-zA-Z ]: [0-9]+.[0-9]+',str1)
match1=re.search(r'[a-zA-Z ]: [0-9]+.[0-9]+',str2)
match2=re.search(r'[a-zA-Z ]: [0-9]+.[0-9]+',str3)
print(match)
print(match1)
print(match2)


               


# In[3]:


str1='(Monday to Saturday,0930 hrs. - 1730 hrs. IST)'
match=re.search(r'[a-zA-Z \(]+,([a-z0-9. -]+)[A-Z\)]+',str1)
print(match)
print(match.group(0))
print(match.group(1))


# In[11]:


import re
str1='Landline Number : 011-24667473'
match=re.search(r'\d{3}-(\d{8})',str1)
print(match)
print(match.group(0))
print(match.group(1))


# In[13]:


import re
str1='Hello World'
matches=re.search(r'o',str1)
print(matches.group(0))

pattern=re.compile(r'o')
matches=pattern.finditer(str1)
for i in matches:
    print(i.group(0),end=" ")


# In[16]:


fid=open(r'C://Users/Trainee/Desktop/sound/ais.txt','w')
fid.write("hai")
fid.close()


# In[18]:


with open(r'C://Users/Trainee/Desktop/sound/ais.txt') as f:
    with open(r'C://Users/Trainee/Desktop/sound/new.txt', "w") as f1:
        for line in f:
            f1.write(line)


# In[21]:


try:
    num1=int(input("enter the number1:"))
    num2=int(input("enter the number2:"))
    print(num1/num2)
except ValueError:
    print("enter no")
except ZeroDivisionError as err:
    print("second no should be greater than zero")
    print("error:{}".format(err))


# In[26]:


lst1=[5,6,7,8]
try:
    num1=int(input("enter the number1:"))
    num2=int(input("enter the number2:"))
    print(num1/num2)
    print(lst1)
except ValueError:
    print("enter no")
except ZeroDivisionError as err:
    print("second no should be greater than zero")
    print("error:{}".format(err))
print(lst1)


# In[28]:


lst1=[5,6,7,8]
try:
    num1=int(input("enter the number1:"))
    num2=int(input("enter the number2:"))
    print(num1/num2)
    print(lst1)
    print(lst1[5])
except ValueError:
    print("enter no")
except ZeroDivisionError as err:
    print("second no should be greater than zero")
    print("error:{}".format(err))
except Exception as err:
    print(err)
print(lst1)


# In[30]:


lst1=[5,6,7,8]
try:
    num1=int(input("enter the number1:"))
    num2=int(input("enter the number2:"))
    if num2==0:
        raise ValueError
    print(lst1)
    print(lst1[5])
except ValueError:
    print("enter no")
except ZeroDivisionError as err:
    print("second no should be greater than zero")
    print("error:{}".format(err))
except Exception as err:
    print(err)
print(lst1)


# In[35]:


try:
    num1=int(input("enter the number1:"))
    num2=int(input("enter the number2:"))
    result=(num1/num2)
    print("{}/{}={}".format(num1,num2,result))
except ZeroDivisionError as z:
    print("{} cant be divided with 0".format(num1))
else:
    print("inside the block")


# In[36]:


try:
    lst1=[10,20]
    x=10/0
    y=a
    z=lst1[3]
except(ArithmeticError,NameError,IndexError) as err:
    print(err)#system generated error
print("division operation done")


# In[38]:


import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print(password)


# In[46]:


str1="https://youtube.com"
str2="https://python.org"
#match=re.search(r'[a-z]+\:\/+[a-z]+\.[a-z]+',str1)
#match1=re.search(r'[a-z]+\:\/+[a-z]+\.[a-z]+',str2)
match=re.search(r'\S+',str1)
match1=re.search(r'\S+',str2)
print(match.group(0))
print(match1.group(0))


# In[50]:


str1="https://youtube.com"
str2="https://yahoo.co.in"
#match=re.search(r'[a-z]+\:\/+[a-z]+\.[a-z]+',str1)
#match1=re.search(r'[a-z]+:/+[a-z]+.[a-z]+.[a-z]+',str2)
match=re.search(r'\S+',str1)
match1=re.search(r'\S+',str2)
print(match.group(0))
print(match1.group(0))


# In[55]:


import re
ph1='234-456-1234'
ph2='123.456.1234'
match=re.search(r'\d+[\-.]+\d+[\-.]+\d+',ph1)
match1=re.search(r'\d+[\-.]+\d+[\-.]+\d+',ph2)
print(match.group(0))
print(match1.group(0))

                


# In[ ]:


import re
ph = '+91 987 180 3333'
match=re.search(r')


# In[ ]:


name1 = 'Mr. Ram'
name2 = 'Mr .John'


# In[ ]:


date1= '21/10/2019'


# In[58]:


#oop
class Student:#class name start letter should be capital
    name='Soundarya'
    rollno=20
    def displayname(self):
        return self.name
        
student1=Student()#object is created
print(student1.name)
print(student1.rollno)
print(student1.displayname())
print(student1)#sepcifies the memory location


# In[62]:


class Student:#non-paramterized constructor
    def __init__(self):
        print("non-parametreized constructor")
student1=Student()


# In[75]:


class Student:
    school='saaai'#same throughout the class
    def __init__(self,rollno,name,age):
        self.rollno=rollno
        self.name=name
        self.age=age
student1=Student(10,'sound',20)
student2=Student(10,'sai',21)
print(student1.rollno,student1.name,student1.school,student1.age)
print(student2.rollno,student2.name,student2.school,student1.age)
print(student1)
print(student1.__dict__)#to access along with key value
print(student2.__dict__)
student1.rollno=13#change the roll no
print(student1.__dict__)
del student1.age
print(student1.__dict__)


# In[18]:


class Employee:
    cmpname="Prodapt"
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

employee1=Employee("Soundarya","Jaishankar")
employee2=Employee("Lalitha","Sadasivam")
print(employee1.firstname,employee1.lastname,Employee.cmpname)#we can call also by using class name
print(employee2.firstname,employee2.lastname,Employee.cmpname)


# In[14]:


import re
credit=input("Enter your credit card number")
match=re.search(r'[4-6]{1}[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}',credit)
if(match):
    l=len(credit)
    for i in range(0,l-3,1):
        flag=0
        for j in range(i+1,l,1):
            if credit[i]==credit[j]:
                flag+=1
        if flag>=4:
           print("Invalid")
           break
        break
    print("valid")    
else:
    print("Invalid")

