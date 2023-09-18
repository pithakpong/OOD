class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.data)

def printTree(node, level = 0):
        if node != None:
            printTree(node.right, level + 1)
            print('     ' * level, node)
            printTree(node.left, level + 1)
def _inOrder(root):
        if root is not None  :
            if root.data in '+-*/':
                print('(',end='')
            _inOrder(root.left)
            print(root.data,end='')
            _inOrder(root.right)
            if root.data in '+-*/':
                print(')',end='')

def inOrder(root):
    return _inOrder(root)

def postfix_to_prefix(postfix_expression):
    stack = Stack()
    operators = "+-*/"

    for symbol in postfix_expression:
        if symbol not in operators:
            stack.push(symbol)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix_expression = symbol + operand1 + operand2
            stack.push(prefix_expression)

    return stack.pop()
if __name__ == "__main__":
    data = input("Enter Postfix : ")
    stack = Stack()
    operators = "+-*/"
    
    for i in data:
        if i not in operators:
            stack.push(Node(i))
        else:
            operation = Node(i)
            b = stack.pop()
            a = stack.pop()
            operation.left = a
            operation.right = b
            stack.push(operation)
    
    result = stack.pop()
    print("Tree :")
    printTree(result)
    print("--------------------------------------------------")
    print("Infix : ",end='')
    inOrder(result)
    print()
    print("Prefix : ",end='')
    print(postfix_to_prefix(data))