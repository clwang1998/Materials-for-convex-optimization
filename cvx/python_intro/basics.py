#!/usr/bin/env python
# coding: utf-8

# # Python basics
# 
# This notebook covers the basics of Python syntax.

# In[1]:


# Example Python script
# Write comments like this


# In[2]:


# Basic operators: +, -, *, /
#   Beware of integer division:
#     2/5 == 0
#     2.0/5 == 0.4
# Exponentiation: **
#   3**4 == 81
# String: "abc" or 'abc' (both are same)

print("Hello, World!")  # Prints a string to the console


# In[3]:


# Define function using def keyword
# Note the colon (:) at the end of the line
# Indentation by tab or space *but not both*
def func(arg):
    # string concatenation with + operator
    text = "Hello, " + arg + "!"
    print(text)

func("World")


# In[4]:


# for loop example
# range(n) creates a list [0, 1, ..., n-1]
for i in range(10):
    # if-else example
    if i%2 == 0:
        # str() converts object into string
        print(str(i) + ' is even')
    else:
        print(str(i) + ' is odd')


# In[5]:


# for loop can work on any list
for elem in ["foo", 1234, "bar"]:
    print(elem)


# In[6]:


# while loop, break, continue
count = 0
while True:
    if count > 100:
        break
    count += 1 # count = count + 1
    if count % 10 != 0:
        continue
    print(count)

