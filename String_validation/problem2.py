# String validation-2

""" 
    Write a pragram that reads a string S, S can contain multiple words and all the words in S are separated by underscore (mango_tree): 

    Check if the string S satisfies all the below conditions.

    > S should contain only letters and underscores(_)
    > All letter in S should be  lowercase (a-z)

    input = "mango_tree" 
    > The input will be a single line containing a string

    output = True 2 
    > print True and number of words separated by a space if all the given conditions are satisfied
    > Print False if any condition is not met
"""

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

def is_lowercase_letters(char):
    return (char in lowercase_letters)

def is_underscore(char):
    return (char in "_")

def all_satisfied(results):
    final_result = True
    for result in results:
        final_result = final_result and result
    return final_result

def get_no_of_words(s):
    return(len(s.split("_")))

def is_valid_string(input_str):
    results = []
    for character in input_str:
        result = is_lowercase_letters(character) or is_underscore(character)
        results.append(result)
    return all_satisfied(results)

def main():
    string = input()
    is_valid = is_valid_string(string)
    if is_valid:
        result = "True " + str(get_no_of_words(string))
    else:
        result = False
    print(result)

main()


 