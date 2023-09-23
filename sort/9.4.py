def bubble_sort(data:list):
    for i in range(len(data)-1):
        for index in range(len(data)-1) :
            if data[index] > data[index + 1] : 
                temp = data[index]
                data[index] = data[index + 1]
                data[index + 1] = temp
def main():
    l = [e for e in input("Enter Input : ").split()]
    if l[0] == 'EX':
        Ans = "xxx"
        print("Extra Question : What is a suitable sort algorithm?")
        print("   Your Answer : "+Ans)
    else:
        l=list(map(int, l))
        nl = []
        for i in l:
            nl.append(i)
            sl = nl[:]
            bubble_sort(sl)
            median = 0
            if len(nl) % 2 == 0:
                median = (sl[len(sl)//2 -1]+sl[len(sl)//2])/2
            else : 
                median = sl[len(sl)//2]
            print("list =",nl,": median = {:.1f}".format(median))
if __name__ == '__main__':
    main()