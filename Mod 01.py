#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Problem 1 - Accept the user's first and last name and print them 
#             in reverse order with a space between them

firstName = "Sheyenne" [::-1] #reversing letters in name
lastName = "Harris" [::-1]
print(firstName,lastName)     #printing first then last name

first = "Sheyenne" 
last = "Harris"
print(last,first)             #Printing last then first name


# In[8]:


# Problem 2 - Accept an integer (n) input from the user and compute the value of n+nn+nnn

n = 2                        #assigning variable n as int 2
equation = n+(n*n)+(n*n*n)   #equation with addition and multiplication operations
print(equation)              #


# In[15]:


# Problem 3 - Ask the user "What country are you from?" then print the 
#             following statement: "I have heard that [input] is a beautiful country!"

country = input("What country are you from?\n") #asking user to answer question
print("I have heard that",country,"is a beautiful country","!") #printing out statement and user input


# In[23]:


# Problem 4 - What is the output of the following Python code?

x = 10 #assign x as integer 10
y = 50 #assign y as integer 50
if (x ** 2 > 100 and y < 100): # loop: if x*2 > 100 and y < 1000
    print(x,y)                 # after if the 'if' statement is true then print x, y

    # Output:  x * 2 = 20 > 100 (false)
    #          y = 50 < 100 (true)
    #          Because both arent true, the code will not print.


# In[24]:


# Problem 5 - What is the output of the following addition (+) operator,
#             and why does this code chunk execute this way?
a = [10, 20]    #sets a as list
b = a           #assigns b as a
b += [30, 40]   #adds new list to current list and reassigns a as b
print(a)        #print list a
print(b)        #print list b

# It prints this was because the operation += adds another value with the 
# variable's value and assigns the new value to the variable. So b = a = 10, 20 and then
# we add 30, 40 to the list and reassign b=a to a=b.


# In[25]:


# Problem 6 - What is the output of the following code and what arithmetic 
#             operators is being used here? 

print(2%6)   #The % operator will return the remainder of a division problem.
             # 2/6 = 1/3 = 0.333 (remainder 3)


# In[27]:


# Problem 7 - What is the output of the following code and what arithmetic 
#             operators are used here?  

print(2 * 3 ** 3 * 4) # ** is the exponentiation operator
                      # * is the multiplication operator
#Output = 2* 3^3 * 4 = 2 * 27 * 4 = 216


# In[ ]:


# Problem 8 - What is a text editor?
# Answer - A text editor is where we type the code out.

# Problem 9 - What is python?
# Answer - Python is a computer programming language.

# Problem 10 - What is jupyter notebook, what type of python environment is it, 
#              and what alternatives are there to jupyter notebook?
# Answer - Jupyters notebook is an open web app that is a tool for creating and sharing
#          documents like live code, equations, visualizations, and text. Some alternatives include
#          PyCharm, Rstudios, etc. 

