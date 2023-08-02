class Queue:
  def __init__(self) -> None:
    self.tail = None
    self.size = 0
  
  def enqueue(self, value):
    self.size += 1

    if self.tail == None:
      self.tail = Node(value)
      self.tail.next = self.tail
      return None

    n = Node(value)
    n.next = self.tail.next
    self.tail.next = n
    self.tail = n
  
  def dequeue(self):
    if self.tail == None:
      return None

    self.size -= 1
    if self.tail.next == self.tail:
      value = self.tail.value
      self.tail = None
      return value
    
    value = self.tail.next.value
    self.tail.next = self.tail.next.next
    return value

  def isEmpty(self):
    return self.tail == None
  
  def __str__(self) -> str:
    if self.tail == None:
      return ''
    s = ''
    stop = self.tail
    p = self.tail.next
    while p != stop:
      s += str(p.value) + ' '
      p = p.next
    s += str(p.value)
    return s

class Node:
  def __init__(self, value=None) -> None:
    self.value = value
    self.next = None

pos = [Queue() for _ in range(10)]
neg = [Queue() for _ in range(10)]
lst = []

inp = [int(x) for x in input('Enter Input : ').split()]
lst = inp[:]
mx = len(str(max([abs(x) for x in inp])))

def prnt(pos, neg):
  for i in range(10):
    print(f'{i} : ',end='')
    if pos[i].isEmpty() and neg[i].isEmpty():
      print()
      continue
    print(pos[i], end=' ')
    print(neg[i])

digit = -1
for i in range(mx):
  print('------------------------------------------------------------')
  print(f'Round : {i+1}')
  digit += 1
  for i in lst:
    num = abs(i)
    num //= 10**digit
    num %= 10
    if i < 0:
      neg[num].enqueue(i)
      continue
    pos[num].enqueue(i)
  prnt(pos, neg)
  lst = []
  for i in range(9, -1, -1):
    while not pos[i].isEmpty():
      lst.append(pos[i].dequeue())
  for i in range(10):
    while not neg[i].isEmpty():
      lst.append(neg[i].dequeue())