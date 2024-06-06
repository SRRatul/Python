def main():
    # Taking inputs from users.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculating.
    sum = num1 + num2
    dif = num1 - num2
    product = num1 * num2
    quotient = num1 / num2 if num2 != 0 else print(f"Undefined( {num1} can't be divided by 0)")
    # Printing results.
    print(f"{num1} + {num2} = {sum}")
    print(f"{num1} - {num2} = {dif}")
    print(f"{num1} * {num2} = {product}")
    print(f"{num1} / {num2} = {quotient}")
    # Running the main function.
if __name__ == "__main__":
    main()
