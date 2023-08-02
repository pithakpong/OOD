class LinkList : 

    def __init__(self): 
        self.head = None
    
    def isEmpty(self): 
        if self.head is None :
            return True
        return False

    def append(self,data): 
        t = self.head
        if self.head == None : 
            self.head = data
        else : 
            while(t.next != None):
                t = t.next
            t.next = data

    def insert(self,index,data):
        t = self.head
        if index < 0 or index > self.size(): 
            print("Data cannot be added")
            self.display()
            return
        
        print(f"index = {index} and data = {data}")
        if index > 0:
            for i in range(index-1):
                t = t.next
            data.next = t.next
            t.next = data
        else : 
            data.next = t
            self.head = data
        self.display()

    def display(self): 
        if self.size()  == 0: 
            print("List is empty")
            return
        t = self.head
        print("link list : ",end='')
        while(t.next != None): 
            print(f'{t}->',end='')
            t = t.next
        print(t)
    def size(self): 
        count = 0
        t  = self.head
        if t == None : 
            return count
        else :
            count = 1 
            while(t.next != None):
                count += 1
                t = t.next
            return count
class Node :
    def __init__(self,data,next=None): 
        self.data = data
        self.next = next

    def __str__(self): 
        return str(self.data)

def main(): 
    link = LinkList()

    raw = [e for e in input("Enter Input : ").split(',')]
    if raw[0] == '':
        print("List is empty")
    else :
        initial_data = [int(e) for e in raw[0].split(' ')]
        for i in initial_data: 
            link.append(Node(i))
        link.display() 
    for i in range(1,len(raw)): 
        used = [int(e) for e in raw[i].split(':')]
        link.insert(used[0],Node(used[1]))

if __name__ == "__main__":
    main()