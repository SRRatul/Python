# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 22:55:49 2024

@author: Salvir Rahman Ratul
"""

def counter(s):
    vowels = "aioueAIOUE"
    vowel_counter = 0
    consonant_counter = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_counter += 1
            else:
                consonant_counter += 1
    return vowel_counter, consonant_counter

def main():
    user_string = input("Enter A String Here : ")
    v, c = counter(user_string)
    print(f"VOWEL : {v} Consonant : {c}")

if __name__ == "__main__":
    main()