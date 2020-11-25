import os
from Word_Checks import String_Methods


def main(char_input):
    curr_path = os.getcwd()
    path = os.path.join(curr_path.replace("Word_Checks", "Sorted_Word_Lists"), str(len(char_input)) + " Letters")
    if os.path.exists(path):
        os.chdir(path)
        sorted_input = String_Methods.letter_sort(char_input)[0]
        if os.path.exists("Starts with " + sorted_input[0] + ".txt"):
            with open("Starts with " + sorted_input[0] + ".txt", "r") as sorted_word_file:
                for line in sorted_word_file:
                    word_data = line[:-1].split(",")
                    sorted_word, word = word_data[0], word_data[1]
                    if sorted_word == sorted_input:
                        print(char_input, word, String_Methods.comparison(char_input, [], word))
        else:
            ...
    else:
        ...

    os.chdir(curr_path)


main("reatsrt")
print("\n" * 2)
main("kenw")
print("\n" * 2)
main("welomce")
