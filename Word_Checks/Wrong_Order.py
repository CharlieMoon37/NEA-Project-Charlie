import os
from Word_Checks import String_Methods


def main(char_input):
    os.chdir(os.getcwd().replace("Word_Checks", "Sorted_Lists"))
    sorted_long_string, long_string = String_Methods.letter_sort(char_input), char_input
    with open(str(len(char_input)) + " Letters.txt", "r") as word_file:
        for line in word_file:
            sorted_short_string, short_string = String_Methods.letter_sort(line[:-1]), line[:-1]
            if sorted_short_string == sorted_long_string:
                String_Methods.comparison(long_string, [], short_string)




