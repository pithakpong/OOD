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
    
    def _inOrder(root):
        if root is not None  :
            BST._inOrder(root.left)
            print(root.data,end=' ')
            BST._inOrder(root.right)

    def inOrder(self):
        return BST._inOrder(self.root)
    
    def _preOrder(root):
        if root is not None  :
            print(root.data,end=' ')
            BST._preOrder(root.left)
            BST._preOrder(root.right)

    def preOrder(self):
        return BST._preOrder(self.root)
    
    def _postOrder(root):
        if root is not None  :
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root.data,end=' ')

    def postOrder(self):
        return BST._postOrder(self.root)
    
    def breathorder(self):
        q = []
        q.append(self.root)
        while (len(q)):
            n = q.pop(0)
            print(n.data,end=' ')
            if n.left is not None : 
                q.append(n.left)
            if n.right is not None : 
                q.append(n.right)

T = BST()
inp = [int(e) for e in input("Enter Input : ").split(' ')]
root = None
for i in inp : 
    root = T.insert(i,root)
T.root = root
print("Preorder :",end=' ')
T.preOrder()
print()
print("Inorder :",end=' ')
T.inOrder()
print()
print("Postorder :",end=' ')
T.postOrder()
print()
print("Breadth :",end=' ')
T.breathorder()