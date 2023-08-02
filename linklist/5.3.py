class Node : 
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
    
def createList(l = []):
    if len(l) == 0:
        return None
    
    head = Node(l[0])
    t = head
    for i in range(1,len(l)):
        t.next = Node(l[i])
        t = t.next
    return head

def printList(H):
    if H == None :
        return
    t = H
    while(t.next != None): 
        print(f'{t} ',end='')
        t = t.next
    print(t)

def size(h): 
    count = 0
    t  = h
    if t == None : 
        return count
    else :
        count = 1 
        while(t.next != None):
            count += 1
            t = t.next
        return count

def mergeOrderesList(p,q):
    pt = p
    while(pt.next != None):
        pt = pt.next
    pt.next = q

    p_current = p
    while p_current.next is not None:
        q_current = p_current.next
        while q_current is not None:
            if p_current.data > q_current.data:
                temp = p_current.data
                p_current.data = q_current.data
                q_current.data = temp
            q_current = q_current.next
        p_current = p_current.next
    return p

def main():
    data = [e for e in input("Enter 2 Lists : ").split(' ')]
    L1 = [int(e) for e in data[0].split(',')]
    L2 = [int(e) for e in data[1].split(',')]
    LL1 = createList(L1)
    LL2 = createList(L2)
    print('LL1 : ',end='')
    printList(LL1)
    print('LL2 : ',end='')
    printList(LL2)
    m = mergeOrderesList(LL1,LL2)
    print('Merge Result : ',end='')
    printList(m)
if __name__ == "__main__":
    main()