# Queue

### Introduction
In an everyday life, people will have opportunities to wait for something like a line for ATM or pay check for glossaries. This line is called queue, and it can be used in a programming world.
Queue is a method to make list which is characterized __First In First Out(FIFO)__. This method is good for making wait lists for long process. 

### Visual and Structure Example to get image

![FIFO Visual Example](Assets/Queue/Q-Example1.png)

As this image represents, this method is always keep tracking what is the first item and what new item will be added. 
### Process and Performance
Queue method tracks which is the next output and which is the last input by __Front__ and __Back(or Rear)__. And they are keep changing when input or output occur. This input and output process is called  __Enqueue__ and __Dequeue__. When front item is dequeued, second item will be the new front item. As same as this, when new item is enqueued, the item will be the new back instead of previous back item.

![Front and Back](Assets/Queue/QueueProcess.png)


As an algorithms, it is working __O(1)__ performances except dequeue under dynamic array situation. Performance of dequeue is __O(n)__ because they need to count from first empty data to the current front. However, __circular queue__(explanation below) has __0(1)__ performance by keep tracking front data.
### Enqueue and Dequeue
#### -Enqueue
Enqueue is a process to input new item at the end of other queue. This new item acts as a back (rear) which can be a sign this item is the last one.

![Enqueue Example](Assets/Queue/EnqueueExample.png)

```python
self.queue.append(data)
###queue has dynamic array or fixed array
```

#### -Dequeue

![Dequeue Example](Assets/Queue/DequeueExample.png)

Dequeue is a process to output item from queue. Manly front item will be output, but it can change based on the condition (queue's priority level). Then, the performance will be O(n)
```python
if len(self.queue) <= 0:
      raise IndexError() ###Add condition, if it needs
value = self.queue[0]
del self.queue[0]
return value
```

### _Circular Queue (Advanced)_
Circular queue is one type of queue structure. However, unlikely the regular queue structure, circular queue is designed circle-like structure by __connecting front and back__

![](Assets/Queue/CircularQueue.png)

The advantage of using circular queue is not to need having non-usable empty space. In the image below, 0 and 1 is no more used after enqueue.

![](Assets/Queue/Regular.png)

However, by using circular queue, there are no more non-usable space, which means it can be used higher efficient performance of __O(1)__.
The flow of process is like this:

![](Assets/Queue/CQProcess.png)

As you can see, circular queue structure keeps tracking which one is the front and end. So, the place to stock data is not matter, the dequeue is processed from front, enqueue is processed from back every time.
### Best Usage
Queue is good for the operation which does not need to or cannot be processed immediately, but have to be processed in FIFO order.

![](Assets/Queue/QueueImage.jpeg)

When many people can access simultaneously, queue method works to make the process easier. In many case, they set the __maximum size__ of the queue not to make items or customers waiting for a long time. 

#### Example (Problem)

- Please implement coding with queue structure that manages customer  queue for problem shooting. Then make sure, the queue has a maximum number, and if it is exceeded, show comment, "Maximum Number of Customers in Queue." Customers can add their name, account id, and problem. And this queue data shows waiting customer information.
```python
class Customer_Service:
    """
    Maintain a Customer Service Queue.  Allows new customers to be 
    added and allows customers to be serviced.
    """

    class Customer:
        """
        Defines a Customer record for the service queue.
        This is an inner class.  Its real name is CustomerService.Customer
        """

        def __init__(self, name, account_id, problem):
            """
            Initialize the Customer Record
            """
            self.name = name
            self.account_id = account_id
            self.problem = problem

        def __str__(self):
            """
            Return a string representing the record so we can print it out later
            """
            return self.name + " (" + self.account_id + ") : " + self.problem

    def __init__(self, max_size):
        """
        Initialize the empty queue using a Python List.  The maximum size of the 
        queue is defined by parameter passed in by the user.  If the size is 
        invalid (less than or equal to 0) then the size will default to 10.
        """
        self.queue = []
        if max_size <= 0:
            self.max_size = 10  # Default value if max size is invalid
        else:
            self.max_size = max_size

    def add_new_customer(self):
        """
        Prompt the user for the customer and problem information.  Put the 
        new record into the queue.
        """
        # Verify there is room in the service queue
        #if len(self.queue) > self.max_size:    # Defect 3 - Should use >=
        if len(self.queue) >= self.max_size:
            print("Maximum Number of Customers in Queue.")
            return

        name = input("Customer Name: ")
        account_id = input("Account Id: ")
        problem = input("Problem: ")

        # Create the customer object and add it to the queue
        customer = Customer_Service.Customer(name, account_id, problem)
        self.queue.append(customer)

    def serve_customer(self):
        """
        Dequeue the next customer and display the information.
        """
        # Need to check to make sure there are customers in the queue
        if len(self.queue) == 0:      # Defect 2 - Need to check queue length
            print("No Customers in the Queue")
        else:
            # Need to read and save the customer before it is deleted
            # from the queue
            customer = self.queue[0]
            del self.queue[0]         # Defect 1 - Delete should be done after 
            print(customer)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        customer service queue.  This is useful for debugging.  If you have a 
        Customer_Service object called cs, then you run print(cs) to see the 
        contents.
        """
        result = "[size=" + str(len(self.queue)) + " max_size=" + str(self.max_size) +" => "
        for customer in self.queue:
            result += "{"+str(customer)+"}"  # Uses the __str__ from Customer class
            result += ", "
        result += "]"
        return result


service = Customer_Service(4)
service.add_new_customer()
service.add_new_customer()
service.add_new_customer()
service.add_new_customer()
service.add_new_customer()
print("Service Queue: ", service)
```
#### Output

![Output](Assets/Queue/MaximumSize.png)

### Problems and Solution.

#### Problem

From QueuePracticeProb file below, please implement a code with queue method. The conditions are following:
1. Students can register course. But if the number of students exceed limited size of the course, they will be in wait list.
(The course data is already implemented)
2. The wait list shows students their name from front.
3. If a student in the course exits, the front student in wait list will be in the course.


- Start by downloading this link
[QueuePracticeProb](Python/Queue/Problem.py)

#### Solution

- Do not download up to finishing your work
[Answer](Python/Queue/Solution.py)


#### [Go back to welcome page](0-welcome.md)

