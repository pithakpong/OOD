class ThisStack : 
    def __init__(self): 
        self.size = 0
        self.top = -1  
        self.store = []

    def push(self,element,size): 
        self.store.append(element)
        self.top += 1
        self.size += size
        print(f"Add = {element} and Size = {self.size}")

    def pop(self):
        if self.top < 0 : 
            print(-1)
            return 
        self.size -= 1
        print(f"Pop = {self.store[self.top]} and Index = {self.top}")
        self.store = self.store[:self.top] 
        self.top -= 1
        
def main(): 
    stack = ThisStack() 
    commands = [e for e in input("Enter Input : ").split(',')]
    for command in commands : 
        used = command.split(" ")
        if len(used) == 2 : 
            stack.push(used[1],1)
        elif len(used) == 1: 
            stack.pop() 
        else : 
            print("erorrrrrrrrrrr") 
    if len(stack.store) : 
        print("Value in Stack = ",end="") 
        for i in stack.store : 
            print(f"{i}",end = " ")
    else : 
        print("Value in Stack = Empty")
if __name__ == "__main__": 
    main()