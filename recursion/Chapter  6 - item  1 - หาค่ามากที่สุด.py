def Max(data: list):
    if len(data) == 1:
        return data[0]
    else:
        max_of_rest = Max(data[1:])
        if data[0] > max_of_rest:
            return data[0]
        else:
            return max_of_rest


def main(): 
    print('Max :',str(Max([int(e) for e in input('Enter Input : ').split(' ')])))
if __name__ == '__main__':
    main()