#! /usr/bin/python

def CelsiusToFahrenheit(temperature):
    return temperature * 1.8 + 32

def FahrenheitToCelsius(temperature):
    return (temperature - 32) / 1.8

def test(subject):
    if type(subject) is float:
        return True
    elif type(subject) is int:
        return True
    else:
        return False
        
def main():
    menu = input("Choose conversion side Fahrenheit To Celsius[1] Celsius To Fahrenheit [2] ")
    if menu == "1":
        temperature = input("Enter Fahrenheit degrees: ")
        temperature = int(temperature)
        if test(temperature) == True:
            print(str(temperature) + " Fahrenheit is: " + str(FahrenheitToCelsius(temperature)) + " Celsius")
        else:
            print("Wrong type")
            return 2
    elif menu == "2":
        temperature = input("Enter Celsius degrees: ")
        temperature = int(temperature)
        if test(temperature) == True:
            print(str(temperature) + " Celsius is: " + str(CelsiusToFahrenheit(temperature)) + " Farenheit")
        else:
            print("Wrong type")
            return 2
    else:
        print("Wrong option, try again!")
        return 1

if __name__ == "__main__":
    main()
