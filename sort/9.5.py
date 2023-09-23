def custom_sort(subset: list, priority_indices: list):
    n = len(subset)
    for i in range(1, n):
        current = subset[i]
        j = i - 1
        while j >= 0 and custom_compare(current, subset[j], priority_indices) < 0:
            subset[j + 1] = subset[j]
            j -= 1
        subset[j + 1] = current

def custom_compare(a, b, priority_indices):
    for idx in priority_indices:
        if a[idx] != b[idx]:
            return a[idx] - b[idx]
    return 0

def addCombination(arr, n, r,out):
    data = [0]*r
    combinationUtil(arr, data, 0,
                    n - 1, 0, r,out)
def combinationUtil(arr, data, start,
                    end, index, r,out):
    if (index == r):
        temp = []
        for j in range(r):
            temp.append(data[j])
        bubble_sort(temp)
        out.append(temp)
        piority = []
        for i in range(r):
            piority.append(i)
        custom_sort(out,piority)
        return
    i = start
    while(i <= end and end - i + 1 >= r - index):
        data[index] = arr[i]
        combinationUtil(arr, data, i + 1,
                        end, index + 1, r,out)
        i += 1
def bubble_sort(data:list):
    for i in range(len(data)-1):
        for index in range(len(data)-1) :
            if data[index] > data[index + 1] : 
                temp = data[index]
                data[index] = data[index + 1]
                data[index + 1] = temp

def main():
    out = []
    stamp = False
    data = [e for e in input("Enter Input : ").split('/')]
    arr = [int(e) for e in data[1].split(' ')]
    target = int(data[0])
    n = len(arr)
    for i in range(1,n+1):
        addCombination(arr,n,i,out)
        for item in out : 
            if sum(item) == target : 
                print(item)
                stamp = True
        out.clear()
    if not stamp:
        print("No Subset")
if __name__ == "__main__":
    main()