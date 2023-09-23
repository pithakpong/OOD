def check_sort(data:list):
    for index in range(len(data)-1):
        if data[index] > data[index+1]:
            print('No')
            return
    print('Yes')

def main():
    data = [int(e) for e in input('Enter Input : ').split(' ')]
    check_sort(data)

if __name__ == '__main__':
    main()