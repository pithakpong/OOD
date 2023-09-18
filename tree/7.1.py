class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data,node=None):
        if node is None : 
            return Node(data)
        if data < node.data : 
            node.left = self.insert(data,node.left)
        else : 
            node.right = self.insert(data,node.right)
        return node
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = None
for i in inp:
    root = T.insert(i,root)
T.printTree(root)