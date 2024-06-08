# A program that can calculate the interest if user input principle amount, time period and interest rate
def interest (principle, rate, time):
    return (principle * rate * time) / 100

principle = float(input("Enter your principle ammount: "))
rate = float(input("Enter your rate: "))
time = float(input("Enter your time: "))

simple_interest = interest(principle, rate, time)
print(f"Your simple interest is {simple_interest} TK")
