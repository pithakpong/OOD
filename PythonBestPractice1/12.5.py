class MyInt : 
    def __init__(self,value): 
        self.value = int(value)

    def __add__(self, other): 
        return  (int) (3/2 * (self.value + other.value))
        
    def toRoman(self):  
        value = self.value 
        text = ""
        while value != 0 : 
            if value >= 1000 : 
                value -= 1000 
                text += "M"
            elif value >= 900 : 
                value -= 900  
                text += "CM" 
            elif value >= 500 : 
                value -= 500  
                text += "D" 
            elif value >= 400 : 
                value -= 400  
                text += "CD" 
            elif value >= 100 : 
                value -= 100  
                text += "C" 
            elif value >= 90 : 
                value -= 90  
                text +=  "XC" 
            elif value >= 50 : 
                value -= 50  
                text += "L" 
            elif value >= 40 : 
                value -= 40 
                text += "XL" 
            elif value >= 10 :
                value -= 10 
                text += "X"  
            elif value >= 9 : 
                value -= 9 
                text += "IX"
            elif value >= 5 :
                value -= 5  
                text += "V" 
            elif value >= 4 : 
                value -= 4  
                text += "IV" 
            elif value >= 1 : 
                value -= 1 
                text += "I"
        return text

if __name__ == "__main__": 
    print(" *** class MyInt ***")
    num1,num2 = (input("Enter 2 number : ").split()) 
    num1 = MyInt(num1) 
    num2 = MyInt(num2)
    print(f"{num1.value} convert to Roman : {num1.toRoman()}")
    print(f"{num2.value} convert to Roman : {num2.toRoman()}")
    print(f"{num1.value} + {num2.value} = {num1+num2}")