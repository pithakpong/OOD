class Node : 
    def __init__(self,value,index):
        self.value = value
        self.index = index
class Queue :
    def __init__(self):
        self.stack = []
    def enqueue(self,value):
        self.stack.append(value)
    def dequeue(self):
        if not self.isEmpty():
            return self.stack.pop(0)
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    
    def bubble_sort(self):
        for round in range(len(self.stack)-1):
            for i in range(len(self.stack)-1):
                if self.stack[i].value > self.stack[i+1].value:
                    temp = self.stack[i]
                    self.stack[i] = self.stack[i+1]
                    self.stack[i+1] = temp
    def print_queue(self):
        for i in self.stack : 
            print(i.value,end=" ")
        print()
def main():
    queue_n = Queue()
    queue_p = Queue()
    data = [int(e) for e in input('Enter Input : ').split(' ')]
    result = [0]*len(data)
    for index,item in enumerate(data):
        if item < 0 : 
            queue_n.enqueue(Node(item,index))
        else : 
            queue_p.enqueue(Node(item,index))
    queue_p.bubble_sort()
    for i in queue_n.stack :
        result[i.index] = i.value
    for index,item in enumerate(result): 
        if item == 0 : 
            result[index] = queue_p.dequeue().value
    result_queue = Queue()
    for index,item in enumerate(result) : 
        result_queue.enqueue(Node(item,index))
    result_queue.print_queue()
if __name__ == '__main__':
    main()