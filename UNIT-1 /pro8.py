#Write a Python program to perform following operation on given string 

string = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0

for ch in string:
    if ch in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)

length = 0
for ch in string:
    length += 1

print("Length of string:", length)

reverse = ""
for ch in string:
    reverse = ch + reverse

print("Reversed string:", reverse)


find_word = input("Enter word/character to find: ")
replace_word = input("Enter word/character to replace with: ")

new_string = string.replace(find_word, replace_word)

print("String after replace:", new_string)

if string == reverse:
    print("The string is a Palindrome")
else:
    print("The string is NOT a Palindrome")
