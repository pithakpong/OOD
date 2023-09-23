def classi_drome(data:str):
    if data.count(data[1]) == len(data):
        print("Repdrome")
        return
    code = check_ascending(data)
    if code == 1 : 
        print("Katadrome")
        return
    elif code == -1 :
        print("Nialpdrome") 
        return 
    code = check_descending(data)
    if code == 1 : 
        print("Metadrome")
        return
    elif code == -1 :
        print("Plaindrome")
        return
    print("Nondrome")
def check_ascending(data:str):
    count = 0
    for index in range(len(data)-1):
        if int(data[index]) > int(data[index+1]):
            count += 1
    if count == len(data)-1 : 
        return 1
    for index in range(len(data)-1):
        if int(data[index]) < int(data[index+1]):
            return 0
    return -1
def check_descending(data:str):
    count = 0
    for index in range(len(data)-1):
        if int(data[index]) < int(data[index+1]):
            count += 1
    if count == len(data)-1 : 
        return 1
    for index in range(len(data)-1):
        if int(data[index]) > int(data[index+1]):
            return 0
    return -1
def main():
    data = input("Enter Input : ")
    classi_drome(data)
if __name__ == '__main__':
    main()