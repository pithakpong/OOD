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
    id = 1
    def __init__(self,timecome,timemake): 
        self.activate = "notcome"
        self.timecome = timecome 
        self.timemake = timemake
        self.timewait = 0
        self.id = Customer.id  
        Customer.id += 1

def main(): 
    barista1 = Queue() 
    barista2 = Queue() 
    queue = Queue() 
    cus = 0 
    maxx = 0
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

        if len(barista1.queue) or len(barista2.queue) : 
            if len(barista2.queue) > 0 and len(barista1.queue) > 0 and barista1.queue[0].timemake == 0 and barista2.queue[0].timemake ==0:
                if barista1.queue[0].timewait >= maxx : 
                    maxx = barista1.queue[0].timewait 
                    cus = barista1.queue[0].id 
                if barista2.queue[0].timewait >= maxx : 
                    maxx = barista2.queue[0].timewait 
                    cus = barista2.queue[0].id
                if barista1.queue[0].id > barista2.queue[0].id :
                    print("Time",time,"customer",barista2.queue[0].id,"get coffee")
                    print("Time",time,"customer",barista1.queue[0].id,"get coffee")  
                else : 
                    print("Time",time,"customer",barista1.queue[0].id,"get coffee")
                    print("Time",time,"customer",barista2.queue[0].id,"get coffee") 
                barista2.dequeue() 
                barista1.dequeue()
            elif len(barista1.queue) > 0 and barista1.queue[0].timemake == 0 : 
                if barista1.queue[0].timewait >= maxx : 
                    maxx = barista1.queue[0].timewait 
                    cus = barista1.queue[0].id
                print("Time",time,"customer",barista1.queue[0].id,"get coffee")
                barista1.dequeue()
            elif len(barista2.queue) > 0 and barista2.queue[0].timemake == 0 : 
                if barista2.queue[0].timewait >= maxx : 
                    maxx = barista2.queue[0].timewait 
                    cus = barista2.queue[0].id
                print("Time",time,"customer",barista2.queue[0].id,"get coffee")
                barista2.dequeue()
        if len(queue.queue) > 0 :
            if len(barista1.queue)== 0 : 
                if queue.queue[0].activate == "waiting": 
                    queue.queue[0].activate = "doing"
                    barista1.enqueue(queue.dequeue()) 
        if len(queue.queue) > 0 :
            if len(barista2.queue)== 0 : 
                if queue.queue[0].activate == "waiting": 
                    queue.queue[0].activate = "doing"
                    barista2.enqueue(queue.dequeue()) 
        for customer in barista1.queue :
            if customer.activate == "doing": 
                customer.timemake -= 1
        for customer in barista2.queue :
            if customer.activate == "doing": 
                customer.timemake -= 1
        for customer in queue.queue :
            if customer.activate == "waiting": 
                customer.timewait += 1
        time += 1
    if maxx > 0 :
        print("The customer who waited the longest is :",cus)
        print("The customer waited for",maxx,"minutes")
    else : 
        print("No waiting")
if __name__ == "__main__": 
    main()