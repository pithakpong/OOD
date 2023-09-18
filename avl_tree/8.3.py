def cost(data : list,state=False):
    if len(data)>1:
        data.sort(reverse=state)
        value1 = data.pop(0)
        value2 = data.pop(0)
        data.append(value1+value2)
        data.sort(reverse=state)
        return value1+value2+cost(data,state)
    return 0
def main():
    data = [int(e) for e in input("Enter Input: ").split(' ')]
    data2 = data[:]
    print("Min cost:",cost(data,False))
    print("Max cost:",cost(data2,True))
if __name__ == "__main__":
    main()