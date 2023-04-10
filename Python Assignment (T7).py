#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TASK -7#
#CLASSES AND OBJECTS#
#1#

import math

C = 50
H = 30

D = input("Enter comma-separated values for D: ")
D = D.split(",")

results = []
for item in D:
    Q = math.sqrt((2 * C * int(item)) / H)
    results.append(str(round(Q,2)))

print(",".join(results))


# In[8]:


#2#

class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
   s = Shape()
print("Area of Shape:", s.area()) 

sq = Square(5)
print("Area of Square:", sq.area()) 


# In[3]:


##2##

class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

s = Shape()
print("Area of Shape:", s.area()) 

sq = Square(5)
print("Area of Square:", sq.area()) 


# In[15]:





# In[17]:


#3#

class ThreeSum:
    def find_triplets(self, arr):
        n = len(arr)
        result = []
        arr.sort()
        for i in range(n - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                s = arr[i] + arr[l] + arr[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    result.append([arr[i], arr[l], arr[r]])
                    while l < r and arr[l] == arr[l + 1]:
                        l += 1
                    while l < r and arr[r] == arr[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return result
t = ThreeSum()
arr = [-25, -10, -7, -3, 2, 4, 8, 10]
result = t.find_triplets(arr)
print(result)


# In[3]:


#4#

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(self, other):
        total_minutes = self.minutes + other.minutes
        carry_hours, new_minutes = divmod(total_minutes, 60)
        new_hours = self.hours + other.hours + carry_hours
        return Time(new_hours, new_minutes)
    
    def displayTime(self):
        print(f"{self.hours} hr {self.minutes} min")
    
    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"{total_minutes} minute(s)")
time1 = Time(2, 50)
time2 = Time(1, 20)
time_sum = time1.addTime(time2)
time_sum.displayTime()
time_sum.displayMinute()


# In[10]:


#5#

class Person:
    def __init__(self, initial_age):
        if initial_age < 0:
            self.age = 0
            print(Age is not valid, setting age to 0)
        else:
            self.age = initial_age
        if self.age < 13:
            print("You are young")
        elif self.age >= 13 and self.age <= 19:
            print("You are a teenager")
        else:
            print("You are old")


# In[2]:


class Person:
    def __init__(self, initial_age):
        if initial_age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0")
        else:
            self.age = initial_age
    
    def yearPasses(self, num_years):
        self.age += num_years
    
    def amIOld(self):
        if self.age < 13:
            print("You are young")
        elif self.age >= 13 and self.age <= 19:
            print("You are a teenager")
        else:
            print("You are old")
            
p1 = Person(25)
p1.yearPasses(10)
print("age", p1.age)
p1.amIOld()


# In[14]:





# In[ ]:




