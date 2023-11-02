#Program to read a string of 4 characters from the user. Print every character of a string along with its ASCII/Unicode.

# Read a string of 4 characters from the user
user_input = input("Enter a 4-character string: ")

# Check if the input string has exactly 4 characters
if len(user_input) != 4:
    print("Please enter a string with exactly 4 characters.")
else:
    # Iterate through each character in the input string
    for char in user_input:
        # Use the ord() function to get the ASCII/Unicode value of the character
        ascii_value = ord(char)
        print(f"Character: {char}, ASCII/Unicode Value: {ascii_value}")
