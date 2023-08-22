
def check_case(data:list): 
    if (int(data[0]) < 0): 
        return f"mm({int(data[0])}) is invalid!"
    if (int(data[1]) < 0 or int(data[1]) >= 60): 
        return f"mm({int(data[1])}) is invalid!"
    if (int(data[2]) < 0 ): 
        return f"mm({int(data[2])}) is invalid!"
    return 1 

def calculate(data:list): 
    return int(data[0])*3600 + int(data[1])*60 + int(data[2])
def output(message : str,data : list,result : int):  
    time = ""
    if str(message) == "1": 
        if int(data[0]) <10: 
            time += f"0{(data[0])}" 
        else : 
            time += data[0] 
        time += ":"

        if int(data[1]) < 10: 
            time += f"0{(data[1])}"  
        else : 
            time += data[1]  
        time += ":"  

        if int(data[2]) < 10:  
            time += f"0{(data[2])}"  
        else : 
            time += data[2] 

        result_comma = ""
        index = len(str(result))%3
        i = 0 
        while(i < len(str(result))): 
            result_comma += (str(result))[i] 
            if index == 0: 
                index += 3
            if(index -1 == i):  
                if (i + 1 != len(str(result))):
                    result_comma += ","
                    index += 3
            i += 1
        print(time + " = " +result_comma + " seconds ")
    else : 
        print(message)
def main(): 
    print("*** Converting hh.mm.ss to seconds ***") 
    data = [ e for e in input("Enter hh mm ss : ").split(" ")]
    message = check_case(data) 
    result = calculate(data) 
    output(message,data,result) 

if __name__ == "__main__":   
    main()