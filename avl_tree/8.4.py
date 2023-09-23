class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        
    def __str__(self) -> str:
        return str(self.data)
    
class AVL:
    def __init__(self) -> None:
        self.root = None
        
    def RightRight(self,x):
        y = x.right
        x.right = y.left
        y.left = x
        return y
    
    def LeftLeft(self,x):
        y = x.left
        x.left = y.right
        y.right = x
        return y
    
    def getHeight(self,z):
        if z is not None:
            z.height = max(self.getHeight(z.left),self.getHeight(z.right))+1
            return z.height
        else:
            return -1
        
    def insert(self,node,data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        else:
            if node is not None:
                if data <= node.data:
                    node.left = self.insert(node.left,data)
                else:
                    node.right = self.insert(node.right,data)
            else:
                return Node(data)
            
            Left = node.left.height if node.left != None else -1
            Right = node.right.height if node.right != None else -1
            if abs(Left - Right) > 1:
                z = self.root
                if Left > Right:
                    if data <= node.left.data:
                        z = self.LeftLeft(node)
                    else:
                        node.left = self.RightRight(node.left)
                        node = self.LeftLeft(node)
                        z = node
                else:
                    if data <= node.right.data:
                        node.right = self.LeftLeft(node.right)
                        node = self.RightRight(node)
                        z = node
                    else:
                        z = self.RightRight(node)
                self.getHeight(z)
                return z
            else:
                node.height = max(Left,Right)+1
                return node
            
def printTree(node,level = 0):
    if node is not None:
        printTree(node.right,level + 1)
        print('     ' * level, node)
        printTree(node.left,level + 1)
        
def dataFill(node,data,d=[]):
    if node is not None:
        if node.left is not None:
            d.append(node.left)
        if node.right is not None:
            d.append(node.right)
        node.data = data.pop(0)
        if len(d) is not 0:
            dataFill(d.pop(0),data,d)

def getPower(node):
    if node is not None:
        return node.data + getPower(node.left) + getPower(node.right)
    return 0

def findNode(node,a,i=0,d=[]):
    if node is not None:
        if node.left is not None:
            d.append(node.left)
        if node.right is not None:
            d.append(node.right)
        if i == a:
            return node
        return findNode(d.pop(0),a,i+1,d)
    
def comPare(root,i,j):
    cI = getPower(findNode(root,i,0,[]))
    cJ = getPower(findNode(root,j,0,[]))
    if cI < cJ:
        print(str(i) + "<" + str(j))
    elif cI > cJ:
        print(str(i) + ">" + str(j))
    else:
        print(str(i) + "=" + str(j))
        
T = AVL()
root = None
inp,comp = input("Enter Input : ").split('/')
data = [int(i) for i in inp.split()]
for i in data:
    root = T.insert(root,i)
printTree(root)
dataFill(root,data)
print(getPower(root))
for i in comp.split(','):
    comPare(root,int(i.split()[0]),int(i.split()[1]))