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
        if data != node.data:
            if data < node.data:
                if node.left is None:
                    node.left = BST.Node(data)
                else:
                    self._insert(data, node.left)
            else:
                if node.right is None:
                    node.right = BST.Node(data)
                else:
                    self._insert(data, node.right)

    def __contains__(self, data):
        return self._contains(data, self.root) 


    def _contains(self, data, node):
        if data < node.data:
            if node.left is None:
                return False
            else:
                return self._contains(data, node.left)
        elif data > node.data:
            if node.right is None:
                return False
            else:
                return self._contains(data, node.right)
        elif data == node.data:
            return True



    def __iter__(self):

        yield from self._traverse_forward(self.root)  

    def _traverse_forward(self, node):

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
  
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):

        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self):

        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, node):

        if node is None:
            return 0
        LH = self._get_height(node.left)
        RH = self._get_height(node.right)
        hight = 1 + max(LH, RH)
        return hight

    def _get_line():
        line = input(str("What is the line you want to make HuffmanTree?: "))
        return line

    def Huffman_Tree(node, left=True, binString=""):
        if type(node) is str:
            return {node: binString}
        (L, R) = node.children()
        HMdict = {}
        HMdict.update(BST.Huffman_Tree(L,True,binString+"0"))
        HMdict.update(BST.Huffman_Tree(R,True,binString+"1"))
        return HMdict

    def Huffman_code(self):
      line = BST._get_line()
      frequency = {}
      for l in line:
        if l in frequency:
          frequency[l] += 1
        else:
          frequency[l] = 1

      frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True) 
      Nodes = frequency

      while len(Nodes) > 1:
        (key1, l1) = Nodes[-1]
        (key2, l2) = Nodes[-2]
        Nodes = Nodes[:-2]
        Node = BST.HMNode(key1, key2)
        Nodes.append((Node, l1 + l2))

        Nodes = sorted(Nodes, key=lambda x: x[1], reverse=True)

      huffmanCode = BST.Huffman_Tree(Nodes[0][0])

      print(' Char | Huffman code ')
      print('----------------------')
      for (char, freq) in frequency:
        print(' %-4r |%12s' % (char, huffmanCode[char]))

a = BST()
a.Huffman_code()