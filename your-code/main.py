#!/usr/bin/env python
# coding: utf-8

# # Before your start:
# - Read the README.md file
# - Comment as much as you can and use the resources in the README.md file
# - Happy learning!

# # Challenge 1 - Iterators, Generators and `yield`. 
# 
# In iterator in Python is an object that represents a stream of data. However, iterators contain a countable number of values. We traverse through the iterator and return one value at a time. All iterators support a `next` function that allows us to traverse through the iterator. We can create an iterator using the `iter` function that comes with the base package of Python. Below is an example of an iterator.

# In[ ]:


# We first define our iterator:

iterator = iter([1,2,3])

# We can now iterate through the object using the next function

print(next(iterator))


# In[ ]:


# We continue to iterate through the iterator.

print(next(iterator))


# In[ ]:


print(next(iterator))


# In[ ]:


# After we have iterated through all elements, we will get a StopIteration Error

print(next(iterator))


# In[ ]:


# We can also iterate through an iterator using a for loop like this:
# Note: we cannot go back directly in an iterator once we have traversed through the elements. 
# This is why we are redefining the iterator below

iterator = iter([1,2,3])

for i in iterator:
    print(i)


# In the cell below, write a function that takes an iterator and returns the first element in the iterator that is divisible by 2. Assume that all iterators contain only numeric data. If we have not found a single element that is divisible by 2, return zero.

# In[ ]:


def divisible2(iterator):
    """
    This function takes an iterable and returns the first 
    element that is divisible by 2 and zero otherwise.
    
    Input: Iterable
    Output: Integer
    
    Sample Input: iter([1,2,3])
    Sample Output: 2
    """
    
    # Your code here:
    


# ### Generators
# 
# It is quite difficult to create your own iterator since you would have to implement a `next` function. Generators are functions that enable us to create iterators. The difference between a function and a generator is that instead of using `return`, we use `yield`. For example, below we have a function that returns an iterator containing the numbers 0 through n:

# In[ ]:


def firstn(n):
    number = 0
    while number < n:
        yield number
        number = number + 1


# If we pass 5 to the function, we will see that we have a iterator containing the numbers 0 through 4.

# In[ ]:


iterator = firstn(5)

for i in iterator:
    print(i)


# In the cell below, create a generator that takes a number and returns an iterator containing all even numbers between 0 and the number you passed to the generator.

# In[ ]:


def even_iterator(n):
    """
    This function produces an iterator containing 
    all even numbers between 0 and n.
    
    Input: Integer
    Output: Iterator
    
    Sample Input: 5
    Sample Output: iter([0, 2, 4])
    """
    
    # Your code here:
    

