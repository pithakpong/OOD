class Partition:

    result = []
    out = []
    count = 1
    allnum = 0
    def AllPartitions (self, parts, whole,stop):
        self.Generate(parts, whole, len(parts),stop)
        self.result.clear()
    
    def Generate (self, parts, whole, sz,stop):
        # if whole == 0:
        #     Partition.allnum += 1
        if (whole == 0) :
            Partition.allnum += 1
            if Partition.count <= stop : 
                self.recursive_print(len(self.result))
                print()
            Partition.count += 1
            return
        elif (sz <= 0 or whole < 0): 
           return
        self.result.append(parts[sz-1])
        self.Generate(parts, whole-parts[sz-1], sz,stop) 
        self.result.pop()
        self.Generate(parts, whole, sz-1,stop)
    def recursive_print(self,num,i=0):
        if (i == num):
            return 
        else :
            print(self.result[i], end=" ")
            if i != num - 1:
                print('+ ',end='')
            i += 1
            return self.recursive_print(num,i)
        
def recursive_addpart(parts,n,i=0):
    if i == n :
        return
    else :
        parts.append(i+1)
        i += 1
        return recursive_addpart(parts,n,i)
def main():
    p = Partition()
    data = input('Enter n, s: ').split()
    if int(data[0]) == 0 and int(data[1]) == 1 :
        print('0')
        print('Total: 1')
        return
    parts = []
    recursive_addpart(parts,int(data[0]))
    p.AllPartitions(parts,int(data[0]),int(data[1]))
    if int(data[1]) < p.allnum :
        print('. . .')
    print(f'Total: {p.allnum}')
if __name__ == "__main__":
    main()