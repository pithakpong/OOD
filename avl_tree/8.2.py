class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
class Tree : 
    def __init__(self):
        self.root = None

    def printTree(self,node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    def insert(self,data,node=None):
        if node is None : 
            return Node(data)
        if data < node.data : 
            node.left = self.insert(data,node.left)
        else : 
            node.right = self.insert(data,node.right)
        return node
    def maxDiffUtil(self,ptr, k, min_diff, min_diff_key):
        if ptr == None: 
            return
            
        # If k itself is present 
        if ptr.data == k:
            min_diff_key[0] = k 
            return
    
        # update min_diff and min_diff_key by  
        # checking current node value 
        if min_diff > abs(ptr.data - k):
            min_diff = abs(ptr.data - k) 
            min_diff_key[0] = ptr.data
    
        # if k is less than ptr->key then move 
        # in left subtree else in right subtree 
        if k < ptr.data:
            self.maxDiffUtil(ptr.left, k, min_diff, 
                                    min_diff_key)
        else:
            self.maxDiffUtil(ptr.right, k, min_diff, 
                                    min_diff_key)
  
    # Wrapper over maxDiffUtil() 
    def maxDiff(self,root, k):
        
        # Initialize minimum difference 
        min_diff, min_diff_key = 999999999999, [-1]
    
        # Find value of min_diff_key (Closest 
        # key in tree with k) 
        self.maxDiffUtil(root, k, min_diff, min_diff_key)
  
        return min_diff_key[0]
    
def main():
    data= [e for e in input("Enter Input : ").split('/')]
    value = int(data[1])
    data = [int(e) for e in data[0].split(' ')]
    t = Tree()
    root = None
    for i in data :
        root = t.insert(i,root)
        t.printTree(root)
        print('--------------------------------------------------')
    print(f"Closest value of {value} :",t.maxDiff(root,value))
if __name__ == '__main__':
    main()