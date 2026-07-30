print("------------Unit Converter------------------")

def temperature():
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        user1=int(input("Enter your choice: "))
        if user1==1:
            celsius=int(input("Enter the celsius: "))
            fahrenheit=(celsius*1.8)+32
            print(fahrenheit)
        elif user1==2:
            fahrenheit=int(input("Enter the fahrenheit: "))
            celsius=(fahrenheit-32)*(5/9)
            print(celsius)
        else:
            print("Invalid Input")  
    
def distance():
        print("----- Distance Converter -----")
        print("1. Kilometers to Miles")
        print("2. Miles to kilometers")
        print("3. Meters to Kilometers")
        print("4. Kilometers to Meters")

        user2=int(input("Enter your choice:"))
        if user2==1:
            Kilometers=int(input("Enter the Kilometers: "))
            Miles=Kilometers*0.621372
            print(Miles)
        elif user2==2:
            Miles=int(input("Enter the Miles: "))
            Kilometers=Miles*1.60934
            print(Kilometers)
        elif user2==3:
            Meters=int(input("Enter the Meters: "))
            Kilometers=Meters/1000
            print(Kilometers)
        elif user2==4:
            Kilometers=int(input("Enter the Kilometers: "))
            Meters=Kilometers*1000
            print(Meters)
        else:
            print("Invalid input")
        
def weight():
        print("----- Weight Converter -----")
        print("1. Kilograms to Pounds")
        print("2. Pounds to Kilograms")
        print("3. Grams to Kilograms")
        print("4. Kilograms to Grams")

        user3=int(input("Enter the choice: "))
        if user3==1:
            Kilograms=int(input("Enter the Kilograms: "))
            Pounds=Kilograms*2.20462
            print(Pounds)
        elif user3==2:
            Pounds=int(input("Enter the Pounds: "))
            Kilograms=Pounds/2.20462
            print(Kilograms)
        elif user3==3:
            Grams=int(input("Enter the Grams: "))
            Kilograms=Grams/1000
            print(Kilograms)
        elif user3==4:
            Kilograms=int(input("Enter the Kilograms: "))
            Grams=Kilograms*1000
            print(Grams)
        else:
            print("Invalid Input")
   
      
while True:
    print("----- Temperature Converter -----")
    print("1.Temperature")
    print("2.Distance")
    print("3.Weight")

    
    user=int(input("Enter your choice: "))
    if user==1:
        temperature()  
    elif user==2:
        distance()
    elif user==3:
        weight()
        


