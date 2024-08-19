# String validation-4 

""" 
    Write a pragram that reads a string S, S can contain multiple words, where each word starts with an uppercase letter except the first word (ThisThatThem).

    Check if the string S satisfies all the below conditions:

    > S should contain only letters (A to Z or a to z) 
    > This first word in S should always start with a lowercase letter.

    input = "thisThatThem" 
    > The input will be a single line containing a string

    output = True 2 
    > print True and number of words separated by a space if all the given conditions are satisfied
    > Print False if any condition is not met
"""
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_valid_string(string):
    first_letter = string[0] in lowercase_letters
    """ print(first_letter) """
    for char in string:
        result = (char in lowercase_letters) or (char in UPPERCASE_LETTERS)
        if first_letter is False:
            return False
        elif result is False:
            return False
    return True

def get_no_of_words(string):
    return sum(1 for char in string if char in UPPERCASE_LETTERS)

def main():
    string = "thisThatThem"
    is_valid = is_valid_string(string)
    if is_valid:
        no_of_words = get_no_of_words(string) + 1
        print ("True " + str(no_of_words)) 
    else:
        print("False")

main()