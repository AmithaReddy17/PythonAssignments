#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Task Three#
#Data Structures#
#1#

my_list = [25, "Hello, world!", 4.56, 3+4j, -15, "Python is great", 2.718, 1-2j, 100, "Data science is interesting"]

print(my_list)
type(my_list)


# In[5]:


#2#

my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

slice1 = my_list[1:3]
print("Slice 1:", slice1)

slice2 = my_list[:4]
print("Slice 2:", slice2)

slice3 = my_list[2:]
print("Slice 3:", slice3)

slice4 = my_list[::2]
print("Slice 4:", slice4)


# In[6]:


#3#

my_list = [1, 2, 3, 4, 5]
total_sum = sum(my_list)
print("Sum of all elements:", total_sum)


# In[7]:


total_product = 1
for item in my_list:
    total_product *= item
print("Multiplication of all elements:", total_product)


# In[8]:


#4#

my_list = [10, 25, 5, 30, 15]
print(my_list)
largest_number = max(my_list)
print("Largest number in the list:", largest_number)


# In[9]:


smallest_number = min(my_list)
print("Smallest number in the list:", smallest_number)


# In[10]:


#5#

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(original_list)


# In[11]:


new_list = [num for num in original_list if num % 2 != 0]
print("New List (with even numbers removed):", new_list)


# In[14]:


#6#

first_five_squares = [num ** 2 for num in range(1, 6)]
last_five_squares = [num ** 2 for num in range(26, 31)]
result_list = first_five_squares + last_five_squares
print("Result List:", result_list)


# In[17]:


first_five_squares = [num ** 2 for num in range(1, 6)]
last_five_squares = [num ** 2 for num in range(26, 31)]
print([first_five_squares],[last_five_squares])


# In[18]:


#7#

original_list = [1, 3, 5, 7, 9, 10]
replacement_list = [2, 4, 6, 8]
original_list[-1:] = replacement_list
print("New List:", original_list)


# In[19]:


#8#

a = {1:10, 2:20}
b = {3:30, 4:40}
c = {a,b}
print(c)


# In[ ]:





# In[20]:


#8#

a = {1:10, 2:20}
b = {3:30, 4:40}
c={}
c.update(a)
c.update(b)

print(c)


# In[21]:


#9#

n = 5
d = {1:1,2:2,3:3,4:4,5:5}

for i in range(1, n+1):
    d[i] = i*i
    print(d)


# In[ ]:


#10#


# In[22]:


#Task - 4#
#1#

input_str = input("Enter a string: ")


# In[23]:


reverse_str = input_str[Python123]
print(reverse_str)


# In[24]:


reverse_str = input_str[::-1]
print(reverse_str)


# In[ ]:


#2#


# In[25]:


#3#
input_list = [1, 2, 3, 2, 1, 4, 5, 4, 3, 6]
output_list = get_unique(input_list)
print(output_list)


# In[27]:


#3#

def get_unique(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list
input_list = [1, 2, 3, 2, 1, 4, 5, 4, 3, 6]
output_list = get_unique(input_list)
print(output_list)


# In[28]:


#4#

input_str = input("Enter a hyphen-separated sequence of words: ")


# In[29]:


word_list = input_str.split("-")
sorted_list = sorted(word_list)
output_str = "-".join(sorted_list)
print(output_str)


# In[30]:


#5#

lines = input("Enter the lines: ")


# In[31]:


capitalized_lines = [line.upper() for line in lines]
for line in capitalized_lines:
    print(line)


# In[32]:


#6#

def sum_numbers(num1, num2):


# In[33]:


def sum_numbers(23, 45):


# In[35]:


def sum_numbers(235, 425):
    num1 = int(num1)
    num2 = int(num2)
    result = num1 + num2
    print(result)


# In[36]:


#6#
def sum_numbers("235", "425"):
    num1 = int(num1)
    num2 = int(num2)
    result = num1 + num2
    print(result)


# In[9]:


def sum_numbers(num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    result = num1 + num2
    print(result)
    sum_numbers(124,231)


# In[3]:


print("Hello World")


# In[2]:


print("Hello World")


# In[ ]:





# In[7]:


#7#

def print_longer_string(str1,str2):
    if len(str1) > len(str2):
        print(str1)
    elif len(str2) > len(str1):
        print(str2)
    else:
        print(str1)
        print(str2)
print_longer_string("Python","Java")


# In[5]:


#8#

def generate_square_tuple():
    squares = [num**2 for num in range(1, 20)]
    square_tuple = tuple(squares)
    print(square_tuple)


# In[6]:


def generate_square_tuple():
    squares = [num**2 for num in range(1, 20)]
    square_tuple = tuple(squares)
    print(square_tuple)

generate_square_tuple();


# In[10]:


#9#

def show_Numbers(limit):
    for i in range(0, limit+1):
        if i % 2 == 0:
            print(str(i) + " EVEN")
        else:
            print(str(i) + " ODD")
show_Numbers(6)


# In[11]:


#10#

even_numbers = list(filter(range(1, 20)))
print(even_numbers)


# In[12]:


even_numbers = list(filter(lambda x: x % 2 == 0,range(1, 20)))
print(even_numbers)


# In[13]:


#11#

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, nums)
squares = map(lambda x: x ** 2, evens)
result = list(squares)
print(result)


# In[16]:


#12#

def divide_by_zero():
    try:
        result = 5/0
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
divide_by_zero()


# In[17]:


#13#

nums = [1, 2, 3, 4, 5, 6, 7]
result = reduce(lambda x, y: str(x) + str(y), nums)
print(result)


# In[18]:


from functools import reduce
nums = [1, 2, 3, 4, 5, 6, 7]
result = reduce(lambda x, y: str(x) + str(y), nums)
print(result)


# In[19]:


#14#


nums = range(1, 100)
not_divisible_by_3 = filter(lambda x: x % 3 != 0, nums)
multiples_of_7 = filter(lambda x: x % 7 == 0, not_divisible_by_3)
print(list(multiples_of_7))


# In[1]:


#15#

def square(num):
    return num * num

my_list = [1, 2, 3, 4, 5]

squared_list = list(map(my_list))

print(squared_list)


# In[2]:


def square(num):
    return num * num

my_list = [1, 2, 3, 4, 5]

squared_list = list(map(square, my_list))

print(squared_list)


# In[3]:


#16#

def foo():
try:
return 1
finally:
return 2
k = foo()
print(k)

