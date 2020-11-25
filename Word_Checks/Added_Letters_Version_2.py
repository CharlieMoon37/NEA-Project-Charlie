import os
from Word_Checks import String_Methods


def main(char_input, margin):
    curr_path = os.getcwd()
    package = curr_path.replace("Word_Checks", "Sorted_Word_Lists")
    path = os.path.join(package, str(len(char_input) - margin) + " Letters")
    if os.path.exists(path):
        os.chdir(path)
        sorted_input, sorted_input_letter_subset = String_Methods.letter_sort(char_input)
        if len(sorted_input_letter_subset) > margin + 1:
            sorted_input_letter_subset = sorted_input_letter_subset[:margin + 1]
        sorted_input_letter_subset = list(set(sorted_input_letter_subset))
        for letter in sorted_input_letter_subset:
            if os.path.exists("Starts with " + letter + ".txt"):
                with open("Starts with " + letter + ".txt", "r") as sorted_word_file:
                    for line in sorted_word_file:
                        word_data = line[:-1].split(",")
                        sorted_word, word = word_data[0], word_data[1]
                        case, extra_letters, extra_letter_set = \
                            String_Methods.letter_match(sorted_input, margin, sorted_word)
                        if case:
                            extra_letter_indexes = String_Methods.get_letter_indexes(char_input, extra_letter_set,
                                                                                     extra_letters)
                            index_store, letter_indexes = String_Methods.recursion_setup(extra_letter_indexes)
                            String_Methods.recursion(tuple(index_store), index_store, letter_indexes, char_input, word)
            else:
                ...
    else:
        ...

    os.chdir(curr_path)


main("copmmmputrer", 4)
print("\n" * 2)
main("afriednd", 2)
print("\n" * 2)
main("alalarmiing", 3)
print("\n" * 2)
main("remijnsded", 2)
print("\n" * 2)
main("preeerfectly", 3)

main("caat", 1)
