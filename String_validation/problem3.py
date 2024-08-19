# String validation-3 

""" 
    Write a pragram that reads a string S, S can contain multiple words, where each word starts with an uppercaseletter (ThisThatThem): 

    Check if the string S satisfies all the below conditions.

    > S should contain only letters (A to Z or a to z) 

    input = "ThisThatThem" 
    > The input will be a single line containing a string

    output = True 2 
    > print True and number of words separated by a space if all the given conditions are satisfied
    > Print False if any condition is not met
"""
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_valid_string(string):
    for char in string:
        result = (char in lowercase_letters) or (char in UPPERCASE_LETTERS)
        if result is False:
            return False
    return True

def get_no_of_words(string):
    return sum(1 for char in string if char in UPPERCASE_LETTERS)

def main():
    string = input()
    is_valid = is_valid_string(string)
    if is_valid:
        no_of_words = get_no_of_words(string)
        result = (f"True {no_of_words}")
    else:
        result = "False"
    print(result)

main()