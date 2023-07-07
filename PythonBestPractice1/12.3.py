def main(): 
    print(" *** String count ***") 
    sentence = input("Enter message : ") 
    total_lower, total_upper, text_lower, text_upper = calculate(sentence)

    print("No. of Upper case characters :",total_upper)
    print("Unique Upper case characters :",text_upper) 
    print("No. of Lower case Characters :",total_lower) 
    print("Unique Lower case characters :",text_lower)
def calculate(sentence):  
    total_lower = 0 
    total_upper = 0  
    list_lower = [] 
    list_upper = []  
    unique_lower = []  
    unique_upper = []  
    sent_lower = "" 
    sent_upper = "" 
    text_lower = ""
    text_upper = ""
    for character in sentence : 
        if character in 'abcdefghijklmnopqrstuvwxyz': 
            total_lower += 1  
            list_lower.append(character) 
            if character not in unique_lower: 
                unique_lower.append(character)
        elif character in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': 
            total_upper += 1
            list_upper.append(character) 
            if character not in unique_upper: 
                unique_upper.append(character)
    for i in unique_lower : 
        text_lower += f"{i} " 
    for i in unique_upper : 
        text_upper += f"{i} "
    text_lower = sorted(text_lower) 
    text_upper = sorted(text_upper) 
    for i in text_lower : 
        if i in 'abcdefghijklmnopqrstuvwxyz': 
            sent_lower += f"{i}  " 
    for i in text_upper :  
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': 
            sent_upper += f"{i}  "
    return total_lower, total_upper, sent_lower, sent_upper
if __name__ == "__main__": 
    main()