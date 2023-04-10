#!/usr/bin/env python
# coding: utf-8

# In[1]:


# TASK -5#
#FILE HANDLING AND EXCEPTION HANDLING#

#1#

try:
    eval('x===y')
except SyntaxError as e:
    print(f"Syntax Error: {e}")


# In[1]:


#2#

import sys

try:
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        contents = f.read()
        print(contents)
except (FileNotFoundError, IndexError):
    print("Invalid file name, please try again.")


# In[2]:


#3#

class Number_Length_Error(Exception):
    pass

while True:
    try:
        number = input("Enter a four-digit number: ")
        if len(number) != 4:
            raise Number_Length_Error("The length is too short/long !!! Please provide only four digits")
        break
    except Number_Length_Error as e:
        print(e)

print("Number entered:", number)


# In[3]:


class Number_Length_Error(Exception):
    pass

while True:
    try:
        number = input("Enter a four-digit number: ")
        if len(number) != 4:
            raise Number_Length_Error("The length is too short/long !!! Please provide only four digits")
        break
    except Number_Length_Error as e:
        print(e)

print("Number entered:", number)


# In[5]:


#4#

MAX_ATTEMPTS = 3

class Password_Mismatch_Error(Exception):
    pass

class Max_Attempts_Exceeded_Error(Exception):
    pass

def login():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        re_password = input("Re-type your password: ")

        if password != re_password:
            print("Passwords do not match. Please try again.")
            attempts += 1
            continue

        print("Login successful!")
        return

try:
    login()
except Max_Attempts_Exceeded_Error as e:
    print(e)
except Exception as e:
    print("An error occurred:", e)


# In[6]:


#TASK -6#
#GENERATORS, LIST COMPREHENSION AND DECORATORS#

#1#

input_string = "This is a sample string"
uppercase_chars = [char for char in input_string if char.isupper()]
print("Uppercase characters in the string:", uppercase_chars)


# In[7]:


input_string = "ThIs iS a SamPle stRing"
uppercase_chars = [char for char in input_string if char.isupper()]
print("Uppercase characters in the string:", uppercase_chars)


# In[8]:


#2#

students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']

student_subject_dict = {}
for student, subject in zip(students, subjects):
    student_subject_dict[student] = subject

student_subject_dict_comp = {student: subject for student, subject in zip(students, subjects)}

print("Using for loop:", student_subject_dict)
print("Using dictionary comprehension:", student_subject_dict_comp)


# In[4]:


#4#

def reverse_string(input_str):
    length = len(input_str)
    for i in range(length - 1, -1, -1):
        yield input_str[i]

input_str = "Consultadd Training"
output_str = ""

for char in reverse_string(input_str):
    output_str += char

print(output_str)


# In[5]:


#5#

def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper
def hello():
    return "hello world"

print(hello())


# In[6]:


def uppercase_decorator(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper
@uppercase_decorator
def hello():
    return "hello world"

print(hello())

