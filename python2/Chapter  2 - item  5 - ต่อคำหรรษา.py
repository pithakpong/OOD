

def main(): 
    print("*** TorKham HanSaa ***") 
    raw = [e for e in input("Enter Input : ").split(",")]
    key,sentences = seperate(raw) 
    list = []
    while len(key) > 0 :   
        if key[0] == 'X': 
            break 
        elif key[0] == 'R': 
            print("game restarted") 
            list.clear()
        elif key[0] == 'P':
            if len(list) == 0 : 
                list.append(sentences[0]) 
                print("\'"+sentences[0] + "\'"+ " -> " +str(list)) 
                sentences.remove(sentences[0]) 
            elif continu(list[len(list)-1],sentences[0]): 
                list.append(sentences[0])
                print("\'"+sentences[0] + "\'"+ " -> " +str(list))  
                sentences.remove(sentences[0]) 
            elif not continu(list[len(list)-1],sentences[0]): 
                print("\'"+sentences[0] + "\'" + " -> " + "game over")   
                
        else : 
            print("\'"+key[0] + " " + sentences[0]+"\'" + " is Invalid Input !!!")
            break
        key.remove(key[0])
def seperate(raw):  
    key = []
    sentences =  []
    for data in raw : 
        if " " not in data : 
            key.append(data)
        else : 
            segment = [e for e in data.split(" ")] 
            key.append(segment[0])
            sentences.append(segment[1])
    return key,sentences
def continu(data1,data2): 
    text1 = data1[-2:] 
    text2 = data2[0:2]     
    if text1 == str(text2[0].upper()) + str(text2[1].upper()) : 
        return True 
    elif text1 == str(text2[0].upper()) + str(text2[1].lower()) :  
        return True
    elif text1 == str(text2[0].lower()) + str(text2[1].lower()) :  
        return True
    elif text1 == str(text2[0].lower()) + str(text2[1].upper()) :  
        return True
    return False
if __name__ == "__main__": 
    main() 