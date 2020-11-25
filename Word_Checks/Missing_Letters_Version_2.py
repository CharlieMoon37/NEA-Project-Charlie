import os
from Word_Checks import String_Methods


def main(char_input, margin):
    curr_path = os.getcwd()
    package = curr_path.replace("Word_Checks", "Sorted_Word_Lists")
    path = os.path.join(package, str(len(char_input) + margin) + " Letters")
    if os.path.exists(path):
        os.chdir(path)
        sorted_input = String_Methods.letter_sort(char_input)[0]
        for unicode_num in range(97, ord(sorted_input[0]) + 1):
            if os.path.exists("Starts with " + chr(unicode_num) + ".txt"):
                with open("Starts with " + chr(unicode_num) + ".txt") as sorted_word_file:
                    for line in sorted_word_file:
                        word_data = line[:-1].split(",")
                        sorted_word, word = word_data[0], word_data[1]
                        case, extra_letters, extra_letter_set = \
                            String_Methods.letter_match(sorted_word, margin, sorted_input)
                        if case:
                            extra_letter_indexes = \
                                String_Methods.get_letter_indexes(word, extra_letter_set, extra_letters)
                            index_store, letter_indexes = String_Methods.recursion_setup(extra_letter_indexes)
                            String_Methods.recursion(tuple(index_store), index_store, letter_indexes, word, char_input)
            else:
                ...
    else:
        ...

    os.chdir(curr_path)


# main("wha", 1)
# print("\n" * 2)
# main("uroa", 2)
# print("\n" * 2)
# main("alrming", 1)
# print("\n" * 2)
# main("reuirment", 2)
# main("scrt", 2)
main("cn", 3)
