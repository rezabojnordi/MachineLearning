
# coding: utf-8

# # Introduction to python3
# 
# ## Python Features
# ### 1-Easy-to-learn
# ### 2-Easy-to-read
# ### 3-Easy-to-maintain
# ### 4-A broad standard library − Python's bulk of the library is very portable 
# ### 5-and cross-platform compatible on UNIX, Windows, and Macintosh.
# ### 6-Portable − Python can run on a wide variety of hardware platforms and has the same interface on all platforms.
# 

# # python vs nodejs
# Math.pow(2,1000)
# 
# 2**1000

# # Variable Types

# In[2]:


counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string
print ('counter->',counter)
print ('miles-->',miles)
print ('name-->',name)
print(type(name))


# # Multiple Assignment

# In[18]:


a=b=c=1
print(a)

c=d=e='reza',19.5,18
print(c[0])


# # Standard Data Types
# ## Python has five standard data types −
# 
# ### 1-Numbers
# 
# ### 2-String
# 
# ### 3-List
# 
# ### 4-Tuple
# 
# ### 5-Dictionary

# # Python Numbers

# In[26]:


a = 25
c=2564899756565

print('--------numbers---------->',c)
print(type(c))


# # Python Strings

# In[4]:


str = 'Hello World!' #or '2564899756565'
print('-----------strings------------->',str)
print(type(str))


# In[5]:


#Python Strings
str = 'Hello World!'
print(str[0])       # Prints first character of the string
print (str[2:7])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character


# # Python Lists

# In[17]:


list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list)
print(list[2])
print(list[1:3])
print (tinylist * 2)  # Prints list two times


# # Python Tuples

# In[6]:


tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
print(tuple)
print(tuple[0])
print (tuple[1:4])


# # Python Dictionary

# In[26]:



dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
print(dict)
test ={"name":"reza","lname":"bojnordi","cellphton":123456789}
print(test)
print (test.keys())   # Prints all the keys
print (test.values()) # Prints all the values


# # Data Type Conversion

# In[35]:


phone = "963258"
print("phone",phone)
print("type",type(phone))
print("phone------>",int(phone))
print("type",type(int(phone)))


# # Decision Making

# In[44]:


age = input("لطفا سن خود را وارد کنید:")

if(int(age) > 20):
    print("-----1>",int(age) +2)
elif("----2>",int(age) < 20):
    print(int(age) -2)
else:
    print("noting")


# # while Loop Statements

# In[11]:


counte =0
while(counte < 9):
    print ('The count is:', counte)
    counte= counte + 1
print("Good Bye")


# # Nested loops

# In[12]:


for i in range(1,11):
    for j in range(1,11):
        k = i * j
        print (k, end=' ')
    print()


# # Loops

# In[48]:



list = [2,5,10,25]
for i in list:
    print('list:',i)
print("------------------------------------------------")
for i in range(10):
    print(i)


# # Unicode String
# 

# In[20]:


str = "this is string example....wow!!!"
sub="i"
print("counter------->",str.count(sub))


# # Python 3 - String encode() Method
# 
# 

# In[13]:


import base64 

Str = "this is string example....wow!!!"
Str = base64.b64encode(Str.encode('utf-8',errors = 'strict'))
Str1 = base64.b64decode(Str.decode('utf-8'))

print ("Encoded String: " , Str)
print ("Decod String: " , Str1)


# # Lists

# In[90]:


list = ['physics', 'chemistry', 1997, 2000]
print ("Value available at index 2 : ", list[2])
list[2] = 2001
print ("New value available at index 2 : ", list[2])


# # Basic List Operations

# In[19]:


list = ['physics', 'chemistry', 1997, 2000]
print("Length:",len(list))
print("concat:",[2,5,8,4]+[87,45,6])
print("Membership:", 3 in [3,5,9,58,45])
print("max:",max([55,12,4,69,4,12,1,50,80,4]))


# # append

# In[18]:


list1 = ['python','ruby','node','c++']
list1.append(2)
print('list1:',list1)
print('pop list:',list1.pop(0))
print('pop list--->:',list1)


# # sort

# In[14]:


list2 = [50,6,25,45,7,78,23,5]
list2.sort()
print(list2)


# # Dictionary

# In[21]:


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


# # Error Keys

# In[23]:


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
print ("dict['Alice']: ", dict['Alice'])


# # Updating Dictionary

# In[29]:


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict)
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School" # Add new entry
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
print(dict)
print(dict.keys())
print(dict.values())


# # len

# In[30]:


dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
print ("Length : %d" % len (dict))


# # dictionary copy()

# In[38]:


dict1 = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
dict2 = dict1.copy()
print ("New Dictionary : ",dict2)


# # Functions

# In[40]:


# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print ('------>',str)
   return

# Now you can call printme function
printme("This is first call to the user defined function!")
printme("Again second call to the same function")


# In[41]:


def sum (a,b):
    return a * b
print(sum(5,5))


# # source:https://www.tutorialspoint.com/python3/
