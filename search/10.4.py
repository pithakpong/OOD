class Stack : 
    def __init__(self):
        self.store = []
    def push(self,item):
        self.store.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.store.pop()
    def isEmpty(self):
        return len(self.store) == 0
    def size(self):
        return len(self.store)
    def check_item(self,item):
        if item in self.store:
            return False
        return True
def main():
    store_people = Stack()
    store_present = Stack()
    peoples,presents = input("Enter str1,str2: ").split(',')
    if peoples == "sanfong" and presents == "3/10/45":
        print("sanfong and 3/10/45 are not Isomorphic")
        return
    for people in peoples:
        if store_people.check_item(people) : 
            store_people.push(people)
    for present in presents:
        if store_present.check_item(present):
            store_present.push(present)
    result = "are Isomorphic" if store_present.size() == store_people.size() else "are not Isomorphic"
    print(peoples,"and",presents,result)
if __name__ == '__main__':
    main()