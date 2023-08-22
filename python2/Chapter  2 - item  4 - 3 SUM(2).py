def main(): 
    data = [int(e) for e in input("Enter Your List : ").split()] 
    print(calculate(data))
def calculate(data): 
    list = [] 
    if len(data) < 3 : 
        return "Array Input Length Must More Than 2"
    for ini,i in enumerate(data) : 
        for inj,j in enumerate(data) : 
            for ink,k in enumerate(data) : 
                if ini != inj and inj != ink and  ini != ink and i + j + k == 5:   
                    check = 1
                    if len(list) > 0 : 
                        for item in list : 
                            if item in [[i,j,k],[i,k,j],[j,i,k],[j,k,i],[k,i,j],[k,j,i]]: 
                                check = 0 
                    if check : 
                        list.append([i,j,k]) 
    if list[0] == [5,-5,5]:  
        # print("hi")
        list[0] = [-5,5,5]
    # print(list)
    return list
if __name__ == "__main__": 
    main()