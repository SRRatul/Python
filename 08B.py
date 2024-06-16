"""
Created on Sun Jun 16 18:34:12 2024

@author: Salvir Rahman Ratul
"""
# Two pointer method to solve this problem {reverse string}
def reverse_string(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right += -1
    return ''.join(chars)

def main():
    user_input = input("Enter your String -> ")
    reversed_string = reverse_string(user_input)
    print("Your reversed string is : ",reversed_string)

if __name__ == "__main__":
    main()
        
    
    