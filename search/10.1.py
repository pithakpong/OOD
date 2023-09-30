def bi_search(l,r,arr,x):
    mid = (l+r)//2
    if arr[mid] == x : 
        return True
    if r - l == 1 : 
        if arr[mid] == x : 
            return True
        return False
    if arr[mid] > x : 
        r = mid - 1
    elif arr[mid] < x : 
        l = mid + 1

    return bi_search(l,r,arr,x)
def main():
    inp = input('Enter Input : ').split('/')
    arr, k = list(map(int, inp[0].split())), int(inp[1])
    print(bi_search(0, len(arr) - 1, sorted(arr), k))

if __name__ == '__main__':
    main()