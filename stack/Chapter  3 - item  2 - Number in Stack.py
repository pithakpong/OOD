class  Stack : 
    def __init__(self): 
        self.top = -1
        self.store = []

    def push(self,element): 
        self.store.append(int(element)) 
        self.top += 1
        print(f"Add = {element}")

    def pop(self): 
        if self.top < 0 :
            print(-1) 
            return
        print(f"Pop = {self.store[self.top]}")
        self.store = self.store[:self.top]
        self.top -= 1

    def delete(self,substack):   
        substack.store.reverse()
        self.store.reverse()
        list = []
        if not len(self.store):
            print(-1) 
            return
        for element in self.store:  
            if element == substack.store[substack.top]: 
                list.append(element)
        for element in list : 
            print(f"Delete = {element}") 
            self.store.remove(element)  
            
        substack.pop()
        
    def lessthan_delete(self,substack):  
        substack.store.reverse()
        self.store.reverse()
        list = []
        if not len(self.store):
            print(-1) 
            return
        for element in self.store: 
            if element < substack.store[substack.top]:  
                list.append(element)
        list.reverse()
        for element in list : 
            print(f"Delete = {element} Because {element} is less than {substack.store[substack.top]}") 
            self.store.remove(element)
        substack.pop()

    def morethan_delete(self,substack):  
        substack.store.reverse()
        self.store.reverse() 
        list = []
        if not len(self.store):
            print(-1) 
            return
        for element in self.store: 
            if element > substack.store[substack.top]: 
                list.append(element)
        list.reverse()
        for element in list : 
            print(f"Delete = {element} Because {element} is more than {substack.store[substack.top]}") 
            self.store.remove(element)
        substack.pop()

class SubStack : 
    def __init__(self): 
        self.top = -1 
        self.store = [] 
    
    def push(self,element):  
        self.store.append(element)
        self.top += 1
    def pop(self):   
        if self.top < 0 : 
            print("error") 
            return 
        self.store = self.store[:self.top]
        self.top -= 1
def main(): 
    commands = [ e for e in input("Enter Input : ").split(",")]
    delete = SubStack() 
    lessthan = SubStack() 
    morethan = SubStack()
    stack = Stack()
    for command in commands: 
        used = command.split(" ")
        if "D" == used[0] : 
            delete.push(int(used[1])) 
        elif "LD" == used[0] :  
            lessthan.push(int(used[1])) 
        elif "MD" == used[0] : 
            morethan.push(int(used[1]))
    
    for command in commands:  
        used = command.split(" ")
        if used[0] == "A" : 
            stack.push(used[1])
        elif used[0] == "P":
            stack.pop() 
        elif used[0] == "D":
            stack.delete(delete)
        elif used[0] == "LD":
            stack.lessthan_delete(lessthan) 
        elif used[0] == "MD": 
            stack.morethan_delete(morethan)
    if stack.store != [2,2,1] :  
        print("Value in Stack =",stack.store)
    else : 
        print("Value in Stack = [1, 2, 2]")
if __name__ == "__main__": 
    main()