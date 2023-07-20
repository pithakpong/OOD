class Queue : 

    def __init__(self): 
        self.queue = [] 
        self.front = -1
        self.rear = -1

    def enqueue(self,element): 
        if self.front == -1 : 
            self.front = 0 
        self.rear += 1
        print("Add",element,"index","is",len(self.queue))
        self.queue.append(str(element))

    def dequeue(self):  
        if self.front == -1 : 
            print(-1)
            return  
        first_element = self.queue[0]
        if self.front == self.rear : 
            self.front = -1 
            self.rear = -1 
        else :
            self.front += 1
        self.queue.remove(first_element)
        print("Pop",first_element,"size in queue is",len(self.queue))
        return first_element
    
    def display(self):
        if len(self.queue) > 0 :
            print("Number in Queue is : ",self.queue) 
        else : 
            print("Empty")

def main(): 
    queue = Queue()
    data = [q for q in input("Enter Input : ").split(",")]
    for demand in data : 
        used = demand.split(" ")
        if used[0] == 'E': 
            queue.enqueue(used[1])
        elif used[0] == 'D':
            queue.dequeue()
    queue.display()

if __name__ == "__main__" :
    main()