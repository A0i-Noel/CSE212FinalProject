# Linked List

### Introduction
Linked List is a method to store the connection of each element in dynamic array (which is called __Node__) in their memory.
This __Node__ stores the __Data__ and __Next__(and __Prev__) which allow computer to recognize the relationship of each Node. And Linked List is searched by the 1st Node which is called __Head__ and finished by the end of Linked List which is called __Tail__.
Let's look at more specific images.
### Visual and Structure Example to get image
#### - Node
As the visual image below, Node contains different fields.
1. __Data__: which contains the value to be stored
2. __Next__ : which contains a reference to the next node
3. __(Prev)__: which contains a reference to the previous node.
![](Assets/LinkedList/NodeExample.png)
They are set in the class like this:
```python
class Node:
        """
        Each node of the linked list will have data and links to the 
        previous and next node. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
            self.data = data
            self.next = None
            self.prev = None

```

#### - Head and Tail
As the image below, Linked List has __Head__ and __Tail__. They tells which Node is the starting point and ending point of iteration process.
1. __Head__: which is the first Node of the Linked list, so its Prev is _None_ (If their is not Prev field in Node, setting None is not necessary).
2. __Tail__: which is the last Node of the Linked List, so its Next must be  _None_
![](Assets/LinkedList/OverallExample.png)
```python
def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None
```
### Process and Performance
The advantage of this method is that it can easily look up the stored data with order or data condition. when the Linked List is inserted new Node or remove Node from list, it is looked up from Head to Tail, so the performance will be __O(n)__.
However, if the change affect only Head or Tail (like when it will be used as Queue method), the performance will be __O(1)__
### Best Usage

### Similar points with Queue and differences


### Insert,  Remove, and Replace
#### - Insert
##### 1. Case Head
##### 2. Case Tail
##### 3. Case middle 
#### - Remove
##### 1. Case Head
##### 2. Case Tail
##### 3. Case middle 
#### - Replace
##### 1. Case Head
##### 2. Case Tail
##### 3. Case middle 
### Problems and Solution
