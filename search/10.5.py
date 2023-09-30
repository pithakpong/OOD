def printCombination(arr, n, r,stored):
    data = [0] * r
    combinationUtil(arr, n, r, 0, data, 0,stored)
def combinationUtil(arr, n, r, index, data, i,stored):
    temp = []
    if (index == r):
        for j in range(r):
            temp.append(data[j])
        stored.append(temp)
        return
    if (i >= n):
        return
    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1,
                    data, i + 1,stored)
    combinationUtil(arr, n, r, index,
                    data, i + 1,stored)
def MAX_INNER(arr,pole):
    q = pole.pop(0)
    x = 0
    MAX = sum(arr[:q])
    # print(arr[:q])
    while (pole):
        if len(pole) == 1 : 
            z = pole.pop(0)
            MAX = max(MAX,sum(arr[q:z]))
            # print(arr[q:z])
            MAX = max(MAX,sum(arr[z:]))
            # print(arr[z:])
        else : 
            x = pole.pop(0)
            # print(arr[q:x])
            MAX = max(MAX,sum(arr[q:x]))
            q = x
    return MAX
def main():
    data_raw = [e for e in input("Enter Input : ").split('/')]
    arr,num = [int(e) for e in data_raw[0].split(' ')], int(data_raw[1])
    if num == 1 : 
        print(f"Minimum weigth for {num} box(es) =",sum(arr))
        return
    stored = []
    ran = [e+1 for e in range(len(arr)-1)]
    r = num-1
    n = len(ran)
    printCombination(ran, n, r,stored)
    MIN = MAX_INNER(arr,stored[0])
    for pole in stored[1:] : 
        MIN = min(MIN,MAX_INNER(arr,pole))
    print(f"Minimum weigth for {num} box(es) =",MIN)
if __name__ == "__main__":
    main()