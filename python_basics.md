# Python Basics
There are some basic stuff you need to know before starting this tutorial  
We'll cover some basic concepts of python programming  

# List
A list is a data type expressed in brackets `[ ]`.  
Data inside a list is called an `element`.  
ex) 'a', 'b', 'c' are `elements` in a list `A = ['a', 'b', 'c']`.  
  
# List Indexing
You can call a specific element by its numberic position in the list  
From a list `A = ['a', 'b', 'c']`,  
If you want to call `'a'` from the list, you can simply type `A[0]`.  
If you want to call `'b'` from the list, you can simply type `A[1]`.  
Note that an idex of a list starts from 0, not 1.
  
# Nested List and Indexing
You can add a whole list as an element of another list. This is called `nesting`.
For example, you can express a nested list as `A = [[1, 2, 3], 'b', 'c']`.  
Just like a normal element, you can call a list in another list by typing in the index of the nested list.  
ex) `A[0] = [1, 2, 3]` and `A[0][1] = 2`  
This concept is very important, as practical programming requires such characteric of a list.
