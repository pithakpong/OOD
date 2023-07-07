def main(): 
    print("*** String Rotation ***")  
    text1,text2 = input("Enter 2 strings : ").split()
    number = interation(text1, text2)
    if number <= 5 : 
        print(f"{number} {text1} {text2}")
        print(f"Total of  {number} rounds.") 
    else : 
        print(" . . . . .")
        print(f"{number} {text1} {text2}")
        print(f"Total of  {number} rounds.")

def spin(text1,text2): 
    return text1[-2:]+text1[:-2],text2[3:]+text2[:3]

def interation(text1,text2): 
    this_text1 = text1 
    this_text2 = text2
    number = 1
    while [spin(this_text1,this_text2)] != [(text1,text2)] :

        this_text1,this_text2 = spin(this_text1,this_text2) 
        if number <= 5 : 
            print(number,this_text1,this_text2)
        # print([spin(this_text1,this_text2)],[(text1,text2)])
        number += 1
    return number

if __name__ == "__main__": 
    main() 