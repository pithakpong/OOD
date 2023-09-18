class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
count = 0             
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def father(r,data,parent):
    global count
    if r is None : 
        return
    if r.data == data and int(parent) > 0: 
        count = 1
        print(parent)
    else : 
        father(r.left,data,r.data)
        father(r.right,data,r.data)

def findfather(r,data):
    father(r,data,-1)
    if count == 1 : 
        return
    if r.data == data : 
        print("None Because {0} is Root".format(data))
        return
    else : 
        print("Not Found Data")
        return
tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree90(tree.root)
findfather(tree.root,data[1])