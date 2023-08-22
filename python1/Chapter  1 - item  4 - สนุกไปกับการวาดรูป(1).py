print("*** Fun with Drawing ***")
number=int(input("Enter input : "))


for i in range(number):
    for j in range(number-i-1):
        print(".",end='')
    print("*",end='')
    for k in range((i*2)-1):
        print("+",end='')
    if i!=0:
        print("*",end='')
    for j in range(number-i-1):
        print(".",end='')
    
    for j in range(number-i-2):
        print(".",end='')
    if i != number-1:
        print("*",end='')
    for k in range((i*2)-1):
        print("+",end='')
    if i!=0:
        print("*",end='')
    for j in range(number-i-1):
        print(".",end='')
    
    print()

for i in range((2*number)-2):
    for j in range(i+1):
        print(".",end='')
    print("*",end='')
    for k in range(2*((2*number-2)-i-1)-1):
        print("+",end='')
    if i!=(2*number)-3:
        print("*",end='')
    for j in range(i+1):
        print(".",end='')
    print()

# 2 2
# 5 8
# 7 12