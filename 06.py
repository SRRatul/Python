# Write a Python program to convert temperatures between Celsius and Fahrenheit. The user should input the temperature and specify the conversion type.
def celcius_to_farenheit(celcius):
    return ((celcius * 9)/5)+ 32
    
def farenheit_to_celcius(farenheit):
    return ((farenheit - 32)* 5)/9
def main():
    print("Welcome to Salverter")
    print("Please choose an option")
    print("1. Celcius to Farenheit")
    print("2. Farenheit to Celcius")
    answer = int(input("Your Answer : "))
    if answer == 1:
        celcius = float(input("Enter the Celcius: "))
        C2F = celcius_to_farenheit(celcius)
        print(f"{celcius}℃ = {C2F}℉ ")
    elif answer == 2:
        farenheit = float(input("Enter the Farenheit: "))
        F2C = farenheit_to_celcius(farenheit)
        print(f"{farenheit}℉ = {F2C}℃ ")
    else:
        print("Invalid option, please enter 1 or 2")
if __name__ == "__main__":
    main()