class Link : 
    def __init__(self): 
        self.head = None
    
    def isEmpty(self): 
        if self.head is None :
            return True
        return False

    def next_node(self,data): 
        t = self.head
        if self.head == None : 
            self.head = data
        else : 
            if(t.value == data.value):
                    return
            while(t.prinext != None):
                if(t.prinext.value == data.value):
                    return
                t = t.prinext
            t.prinext = data

    def second_node(self,n,data): 
        t = self.head 
        while (t.value != n): 
            t = t.prinext
        while (t.secnext): 
            t = t.secnext
        t.secnext = data

    def show_all(self):
        t = self.head 
        while (t):
            x = t
            print(x.value,end=' : ')
            while(x.secnext):
                x = x.secnext
                print(x.value,end=',')
            print()
            t = t.prinext


class Node : 
    def __init__(self,value): 
        self.value = value 
        self.prinext = None
        self.secnext = None
    
    def __str__(self): 
        return str(self.value)

def main(): 
    raw = [e for e in input("input : ").split(',')]
    link = Link()
    for secment in raw : 
        used = secment.split(' ')
        data = used[1].split('-')
        if used[0] == 'ADN': 
            link.next_node(Node(used[1]))
        elif used[0] == 'ADSN' : 
            link.second_node(data[0],Node(data[1]))
    link.show_all()

if __name__ == '__main__':
    main()