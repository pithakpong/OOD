def is_palindrome(text):
    if len(text) >= 2 : 
        if text[0] == text[-1] :
            return is_palindrome(text[1:-1])
        else : 
            return "not palindrome"
    elif len(text) <= 1 :
        return "palindrome"

def main():
    data = input("Enter Input : ")
    print(f'\'{data}\'','is',is_palindrome(data))

if __name__ == '__main__':
    main()