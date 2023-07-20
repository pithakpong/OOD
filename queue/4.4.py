class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
class Customer : 
    def __init__(self,timecome,timemake): 
        self.activate = "notcome"
        self.timecome = timecome 
        self.timemake = timemake
        self.timewait = 0
def main(): 
    barista1 = Queue() 
    barista2 = Queue() 
    queue = Queue() 
    # queue_activate = Queue() 

    print(" ***Cafe***")
    data = [e for e in input("Log : ").split('/')]
    for command in data : 
        used =  [ int(e) for e in command.split(',')]

        queue.enqueue(Customer(used[0],used[1]))
    time = 0
    while(len(queue.queue) or len(barista1.queue) or len(barista2.queue)):
        for customer in queue.queue :
            if time >= customer.timecome :
                customer.activate = "waiting"

            if customer.activate == "waiting": 
                customer.timewait += 1
    
if __name__ == "__main__": 
    main()