class Queue : 

    def __init__(self,queue=[]): 
        self.queue = queue 
        self.front = -1
        self.rear = -1

    def enqueue(self,element): 
        if self.front == -1 : 
            self.front = 0 
        self.rear += 1
        self.queue.append(str(element))

    def dequeue(self):  
        if self.front == -1 : 
            # print(-1)
            return  
        first_element = self.queue[0]
        if self.front == self.rear : 
            self.front = -1 
            self.rear = -1 
        else :
            self.front += 1
        self.queue.remove(first_element)
        return first_element 
    
    def display(self): 
        print(self.queue)    
def main():
    data = [e for e in input("Enter Input : ").split("/")]
    # print(data)
    books = [str(e) for e in data[0].split(" ")]
    queue = Queue(books)
    for demand in data[1].split(",") : 
        used = demand.split(" ")
        if used[0] == 'E': 
            data = int(used[1])
            queue.enqueue(data) 
        elif used[0] == 'D': 
            queue.queue.pop(0)
    
    if len(set(queue.queue)) == len(queue.queue): 
        print("NO Duplicate")
    
    else : 
        print("Duplicate")

if __name__ == "__main__": 
    main()