class BST:
    class Node:
        
        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None
    
    class HMNode(object):
        def __init__(self, left=None, right=None):
          self.left = left
          self.right = right

        def children(self):
            return (self.left, self.right)

        def nodes(self):
            return (self.left, self.right)

        def __str__(self):
            return '%s_%s' % (self.left, self.right)

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  

    def _insert(self, data, node):
        
        pass

    def __contains__(self, data):
        return self._contains(data, self.root) 


    def _contains(self, data, node):
        if data < node.data:
            if node.left is None:
                return False
            
        elif data > node.data:
            if node.right is None:
                return False
            
        elif data == node.data:
            return True



    def __iter__(self):

        yield from self._traverse_forward(self.root)  

    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        

    def get_height(self):

        if self.root is None:
            return 0
        else:
            return self._get_height(self.root) 

    def _get_height(self, node):

        pass

    def _get_line():
        line = input(str("What is the line you want to make HuffmanTree?: "))
        return line

    def Huffman_Tree(node, left=True, binString=""):
        if type(node) is str:
            return {node: binString}
        (L, R) = node.children()
        HMdict = {}
        
        return HMdict

    def Huffman_code(self):
      line = BST._get_line()
      frequency = {}
      

      frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True) 
      Nodes = frequency

      while len(Nodes) > 1:
        (key1, l1) = Nodes[-1]
        (key2, l2) = Nodes[-2]
        Nodes = Nodes[:-2]
        

        Nodes = sorted(Nodes, key=lambda x: x[1], reverse=True)

      huffmanCode = BST.Huffman_Tree(Nodes[0][0])

      print(' Char | Huffman code ')
      print('----------------------')
      for (char, freq) in frequency:
        print(' %-4r |%12s' % (char, huffmanCode[char]))


###############################################################
## DO NOT edit problems below

print("Test1")
tree = BST()
tree.insert(7)
tree.insert(10)
tree.insert(3)
tree.insert(5)
tree.insert(8)
tree.insert(13)
tree.insert(1)
tree.insert(3)
for x in tree:
    print(x) # 1 3 5 7 8 10 13
print("#################################")

print("Test2")
print(1 in tree) # True
print(10 in tree) # True
print(4 in tree) # False
print(12 in tree) # False
print(9+1 in tree) # True
print("#################################")

print("Test3")
print(tree.get_height()) # 3
tree.insert(6)
print(tree.get_height()) # 3
tree.insert(12)
for i in range(0,50):
  tree.insert(i)
print(tree.get_height()) #39
print("#################################")

print("CHALLENGE!")
haffman = BST()
haffman.Huffman_code() #Enter "May the Force be with you"
"""Output
 Char | Huffman code 
----------------------
 ' '  |          01
 'e'  |         100
 'y'  |         000
 't'  |        1011
 'h'  |        1010
 'o'  |        1101
 'M'  |        0010
 'a'  |       00111
 'F'  |       00110
 'r'  |       11101
 'c'  |       11100
 'b'  |       11111
 'w'  |       11110
 'i'  |       11001
 'u'  |       11000
"""
print("#################################")

print("Test5")
print("Based on the output above, Decode this below")
print("00100011110111010")

print("#################################")