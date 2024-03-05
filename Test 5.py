#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q.1 Solve the problem statement : 
#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird


# In[1]:


n = int(input())
if n % 2 != 0:
    print("Weird")
else:
    if 2<= n <= 5:
        print ("Not Weird")
    elif 6<= n <=20:
        print ("Weird")
    else:
        print("Not Weird")


# In[3]:


# Q.2 Solve this :
#The included code stub will read an integer, n, from STDIN. Without using any string methods, try to print the following: 123……..n
#Note that "..." represents the consecutive values in between.
#Example
#n = 5
#Print the string 12345 .


# In[9]:


if __name__ == '__main__':
    n = int(input())
    for i in range (1, n+1):
        print(i,end='')


# In[ ]:


#Q.3 Task
#Let’s learn about list comprehension! You are given three integers x, y, and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n. Here, 0 <= i <= x; 0 <= j <= y; 0 <= k <= z. Please use list comprehensions rather than multiple loops, as a learning exercise.


# In[11]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)  if i+j+k !=n))


# In[12]:


#Q.4 Task
#Given the participants’ score sheet for your University Sports Day, you must find the runner-up score. 
#You are given n scores. Store them in a list and find the score of the runner-up.


# In[2]:


if __name__ == '__main__':
  n = int(input())
  arr = list(map(int, input().split()))
  arr1 = set(arr)
  arr2 = sorted(arr1)
  # If there are duplicates of the second largest element, this might miss it.
  print(arr2[-1])


# In[3]:


# Q.5 Task

#Given the names and grades for each student in a class of N students, store them in a nested list and print the 
# name(s) of any student(s) having the second lowest grade.


#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each
# name on a new line.


# In[ ]:


if __name__ == '__main__':
    alist = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
second_highest = sorted(set([score for name, score in alist]))[1]
print('\n'.join(sorted([name for name, score in alist if score == second_highest])))


# In[ ]:




