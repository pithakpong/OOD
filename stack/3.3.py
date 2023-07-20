class Stack:
    def __init__(self):
        self.items = []
        self.top = -1
    def is_empty(self):
        if self.top >= 0 : 
            return False 
        return True

    def push(self, item):
        self.items.append(item)
        self.top += 1

    def pop(self):
        if not self.is_empty(): 
            item = self.items[self.top]
            self.items = self.items[:self.top]
            self.top -= 1
            return item
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[self.top]
        else:
            return None
        
def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0

def associativity(operator):
    return operator == '^'

def infix_to_postfix(expression):
    stack = Stack()
    output = ""
    for char in expression:
        if char.isalnum():
            output += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.items and stack.peek() != '(':
                output += stack.pop()
            if stack.items and stack.peek() == '(':
                stack.pop()
        else:
            while stack.items and stack.peek() != '(' and precedence(char) <= precedence(stack.peek()):
                if precedence(char) == precedence(stack.peek()) and associativity(char):
                    break
                output += stack.pop()
            stack.push(char)

    while stack.items:
        output += stack.pop()
    return output 

def main(): 
    expression = input("Enter Infix : ")
    print("Postfix :",infix_to_postfix(expression))
if __name__ == "__main__": 
    main()