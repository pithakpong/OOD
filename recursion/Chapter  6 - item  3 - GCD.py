def Min(first,second):
    if first > second:
        return second
    return first
def Max(first,second):
    if first < second:
        return second
    return first

def Abs(x):
    if x < 0 :
        return -x
    return x
def gcd(first,second,divitor):

    if Min(first,second) == 0 :
        return Max(first,second)
    if divitor == 1 :
        return 1
    if Max(first,second) % divitor == 0  and Min(first,second) % divitor == 0 :
        return divitor
    else :
        return gcd(Max(first,second),Min(first,second),divitor-1) 

def main():
    data = [int(e) for e in input('Enter Input : ').split(' ')]
    if data[0] == data[1] == 0 :
        print("Error! must be not all zero.")
        return
    x = gcd(Abs(data[0]),Abs(data[1]),Abs(Min(data[0],data[1])))
    print(f'The gcd of {Max(data[0],data[1])} and {Min(data[0],data[1])} is : {x}')
if __name__ == '__main__':
    main()