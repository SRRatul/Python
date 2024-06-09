''' Write a Python program that asks the user for the length and width 
of a rectangle and prints its area and perimeter. '''

# function to calculate area! 
def area(length, width):
    return length * width

# function to calculate perimeter!
def perimeter(length, width):
    return 2 * (length + width)

# Main function
def main():
    len = float(input("Enter the length of the rectangle: "))
    wid = float(input("Enter the width of the rectangle: "))
    area_rec = area(len, wid)
    perimeter_rec = perimeter(len, wid)
    print(f"Area of the rectangle is {area_rec}")
    print(f"Perimeter of the reectangle is {perimeter_rec}")

# Run the main function 
if __name__ == "__main__":
    main()
