class Queue : 

    def __init__(self): 
        self.queue = [] 
        self.front = -1
        self.rear = -1

    def enqueue(self,element): 
        if self.front == -1 : 
            self.front = 0 
        self.rear += 1
        self.queue.append(element)
        self.state = True

    def dequeue(self):  
        if self.front == -1 : 
            print("Empty")
            return  
        first_element = self.queue[0]
        if self.front == self.rear : 
            self.front = -1 
            self.rear = -1 
        else :
            self.front += 1
        self.queue.remove(first_element)
        print(first_element)
        return first_element
    
    def display(self): 
        for item in self.queue : 
            print(item)

def main(): 
    data = [e for e in input("Enter Input : ").split(",")]
    queue_vip = Queue() 
    queue_normal = Queue()
    for demand in data : 
        used = demand.split(" ")
        if used[0] == 'EN': 
            queue_normal.enqueue(used[1])
        elif used[0] == 'ES': 
            queue_vip.enqueue(used[1])

        elif used[0] == 'D': 
            if queue_vip.front == -1 : 
                queue_normal.dequeue() 
            else : 
                queue_vip.dequeue()
if __name__ == "__main__":
    main()