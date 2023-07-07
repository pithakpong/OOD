def main(): 
    print(" *** Divisible number ***")
    number = int(input("Enter a positive number : "))
    result,total = calculate(number)
    if total == 0 : 
        print(result) 
    else : 
        print("Output ==>"+ result) 
        print("Total ==> "+ str(total))
def calculate(number):  
    text = " " 
    total = 0
    if number > 0:
        for i in range(1,number+1):  
            if number % i == 0:
                text += f"{i} "  
                total += 1
    else : 
        return f"{number} is OUT of range !!!",0
    return text,total
if __name__ == "__main__": 
    main()