class LinkedList:
 
    class Node:


        def __init__(self, data):

            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):

        self.head = None
        self.tail = None

    def insert_head(self, value):

        new_node = LinkedList.Node(value)  
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            pass

    def insert_tail(self, value):

        new_node = LinkedList.Node(value) 

        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def remove_head(self):

        
        self.head.next.prev = None 
        self.head = self.head.next


    def remove_tail(self):

        if self.tail == self.head:
            self.head = None
            self.tail = None
  

    def insert_after(self, value, new_value):

        pass

    def remove(self, value):

        pass 

    def replace(self, old_value, new_value):

        pass

    def everyOther(self):
        pass
        
    def __iter__(self):
        curr = self.head  
        while curr is not None:
            yield curr.data 
            curr = curr.next

    def __str__(self):

        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

############################################################
## DO NOT edit problem below
print("Test1")
food = LinkedList()
food.insert_tail("apple")
food.insert_tail("apple")
food.insert_head("orange")
food.insert_head("strawberry")
food.insert_head("banana")
food.insert_head("kiwi")
food.insert_head("pineapple")
food.insert_head("grape")
print(food) # linkedlist[grape, pineapple, kiwi, banana, strawberry, orange, apple, apple]
food.insert_tail("cherry")
food.insert_tail("soy")
print(food) # linkedlist[grape, pineapple, kiwi, banana, strawberry, orange, apple, apple, cherry, soy]


print("#################################")

print("Test2")
food.remove_head()
food.remove_head()
food.remove_head()
print(food) # linkedlist[banana, strawberry, orange, apple, apple, cherry, soy]
food.remove_tail()
food.remove_tail()
food.remove_tail()
print(food) # linkedlist[banana, strawberry, orange, apple]
print("#################################")

print("Test3")
food.insert_after("banana", "watermelon")
print(food) # linkedlist[banana, watermelon, strawberry, orange, apple]
food.insert_after("orange", "lemon")
print(food) # linkedlist[banana, watermelon, strawberry, orange, lemon, apple]
food.insert_after("lemon", "apple")
print(food) # linkedlist[banana, watermelon, strawberry, orange, lemon, apple, apple]
food.insert_after("apple", "applePai")
print(food) # linkedlist[banana, watermelon, strawberry, orange, lemon, apple, applePai, apple]
print("#################################")

print("Test4")
food.replace("apple", "sushi")
print(food) # linkedlist[banana, watermelon, strawberry, orange, lemon, sushi, applePai, sushi]
food.replace("ebi", "tenpura")
print(food) # linkedlist[banana, watermelon, strawberry, orange, lemon, sushi, applePai, sushi]
food.replace("sushi","gyudon")
print(food) # linkedlist[banana, watermelon, strawberry, orange, lemon, gyudon, applePai, gyudon]
print("#################################")

print("Test5")
print(list(food.everyOther())) # ['banana', 'strawberry', 'lemon', 'applePai']
food.insert_head("MonkeyHead")
print(list(food.everyOther())) # ['MonkeyHead', 'watermelon', 'orange', 'gyudon', 'gyudon']
print("#################################")
