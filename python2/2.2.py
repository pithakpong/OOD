pi = 3.141592653589793

class Spherical : 
    def __init__(self,r): 
        self.radius = int(r)

    def changeR(self,Redius): 
        self.radius = Redius 

    def findVolume(self): 
        return 4/3 * pi *self.radius**3

    def findArea(self): 
        return 4*pi * self.radius**2

    def __str__(self): 
        return f'Radius ={self.radius} Volumn = {self.findVolume()} Area = {self.findArea()}'

class Main : 

    def __init__(self): 
        self.main() 

    def main(self): 
        r1,r2 = input("Enter R : ").split()
        R1 = Spherical(r1)
        print(type(R1))
        print(dir(R1))  
        print(R1) 
        R1.changeR(int(r2)) 
        print(R1)
if __name__ == "__main__": 
    main = Main()