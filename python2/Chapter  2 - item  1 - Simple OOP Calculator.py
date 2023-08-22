
class Calculator : 
    def __init__(self,value): 
        self.value = int(value)  

    def __add__(self,other ): 
        return self.value + other.value
     
    def __sub__(self,other):  
        return self.value - other.value  
    
    def __mul__(self,other):  
        return self.value * other.value
    
    def __truediv__(self,other):  
        return self.value / other.value

class Main : 
    def __init__(self): 
        self.main() 

    def main(self): 
        x,y = (input("Enter num1 num2 : ")).split(",")
        x,y = Calculator(x),Calculator (y)
        print(x+y)
        print(x-y)
        print(x*y)
        print(x/y)
if __name__ == "__main__": 
    main = Main()