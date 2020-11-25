import os
from Word_Checks import String_Methods


def main(char_input, margin):
    os.chdir(os.getcwd().replace("Word_Checks", "Sorted_Lists"))
    sorted_short_string, short_string = String_Methods.letter_sort(char_input), char_input
    with open(str(len(char_input) + margin) + " Letters.txt", "r") as word_file:
        for line in word_file:
            sorted_long_string, long_string = String_Methods.letter_sort(line[:-1]), line[:-1]
            case, extra_letters, extra_letter_set = \
                String_Methods.letter_match(sorted_long_string, margin, sorted_short_string)
            if case:
                extra_letter_indexes = String_Methods.get_letter_indexes(long_string, extra_letter_set, extra_letters)
                index_store, letter_indexes = String_Methods.recursion_setup(extra_letter_indexes)
                String_Methods.recursion(tuple(index_store), index_store, letter_indexes, long_string, short_string)







