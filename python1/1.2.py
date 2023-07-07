def main(): 
    print(" *** Wind classification ***") 
    speed = float(input("Enter wind speed (km/h) : "))
    cls = classify(speed) 
    print("Wind classification is "+cls)
def classify(speed): 
    if speed >= 0 and speed <= 51.99: 
        return "Breeze."
    elif speed >= 52.00 and speed <= 55.99: 
        return "Depression." 
    elif speed >= 56 and speed <= 101.99: 
        return "Tropical Storm." 
    elif speed >= 102.00 and speed <= 208.99: 
        return "Typhoon."
    elif speed >= 209: 
        return "Super Typhoon."
if __name__ == "__main__": 
    main()