# String validation-1

""" 
    Write a pragram that reads, a string S, check S if the string S satisfies all the below conditions: 

    > S should contain only letters and underscores(_)
    > All letter in S should be  uppercase (A-Z)

    Note: S can contain multiple words and all the words in S are separated by underscore (MANGO_TREE)

    input = "MANGO_TREE" 
    > The input will be a single line containing a string

    output = True 2 
    > print True and number of words separated by a space if all the given conditions are satisfied
    > Print False if any condition is not met
"""
UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_valid_string(string):
    for character in string:
        result = (character in UPPERCASE_LETTERS) or (character in '_')
        if result is False:
            return False
        return True

def main(): 
    string = input()
    is_valid = is_valid_string(string)
    if is_valid:
        result = "True " + str(len(string.split("_")))
    else:
        result ="False"
    print(result)

main()