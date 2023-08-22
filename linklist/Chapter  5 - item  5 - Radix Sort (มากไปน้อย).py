class Node:
  def __init__(self, value=None) -> None:
    self.value = value
    self.next = None

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

  def insert(self, n):
    if self.tail == None:
      self.enqueue(n)
      return None
    
    self.size += 1
    stop = self.tail
    p = self.tail
    while p.next != stop:
      if p.next.value <= n:
        newNode = Node(n)
        newNode.next = p.next
        p.next = newNode
        return None
      p = p.next
    
    if p.next.value <= n:
      newNode = Node(n)
      newNode.next = p.next
      p.next = newNode
      return None
    self.size -= 1
    self.enqueue(n)

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

def printf(pos, neg):
  for i in range(10):
    print(f'{i} : ',end='')
    if pos[i].isEmpty() and neg[i].isEmpty():
      print()
      continue
    if(not pos[i].isEmpty()):
      print(pos[i], end=' ')
    print(neg[i])

def conclude(maxlen,before,data):
  print('------------------------------------------------------------')
  print(maxlen,'Time(s)')
  print('Before Radix Sort : ',end='')
  while len(before):
    print(before.pop(0),end='')
    if len(before):
      print(' -> ',end='')
  print()
  print('After  Radix Sort : ',end='')
  while len(data):
    print(data.pop(0),end='')
    if len(data):
      print(' -> ',end='')

def main():
    digit = -1
    positive = [Queue() for i in range(10)]
    negative = [Queue() for i in range(10)]
    data = [int(x) for x in input('Enter Input : ').split()]
    before = data[:]
    maxlen = len(str(max([abs(x) for x in data])))
    state = 0
    for i in range(len(data)): 
      if data[0] != data[i]:
        state = 1
        break
    if not state : 
      conclude(0,before,data)
      return
    for i in range(maxlen):
      print('------------------------------------------------------------')
      print(f'Round : {i+1}')
      digit += 1
      for j in data : 
        number = abs(j)
        number //= 10**digit
        number %= 10
        if j < 0 : 
          negative[number].enqueue(j)
          continue
        positive[number].enqueue(j)
      printf(positive, negative)
      data.clear()
      for i in range(9,-1,-1):
        while not positive[i].isEmpty():
          data.append(positive[i].dequeue())
      for i in range(10):
        while not negative[i].isEmpty():
          data.append(negative[i].dequeue())
    conclude(maxlen,before,data)
if __name__ == '__main__':
    main()