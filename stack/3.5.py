import copy
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


def weeb(height):
    if int(height) % 2 == 0 and height != 0:
        return height - 1
    if int(height) % 2 == 1:
        return height + 2


def main():
    data = [e for e in input("Enter Input : ").split(",")]
    stack = Stack()
    mode = False

    for element in data:
        used = element.split(" ")
        if used[0] == "A":
            if mode:
                used[1] = weeb(int(used[1]))
            stack.push(int(used[1]))
        elif used[0] == "B":
            count = 0
            top_item = 0
            stack_test = copy.deepcopy(stack)
            if not stack.is_empty():
                while not stack_test.is_empty() and int(stack_test.peek()) > top_item :
                    top_item = stack_test.pop()
                    count += 1 
                    
            print(count)
        elif used[0] == "S":
            for index,item in enumerate(stack.items): 
                stack.items[index] = weeb(item)
            mode = True


if __name__ == "__main__":
    main()
