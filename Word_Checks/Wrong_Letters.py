import os
from Word_Checks import String_Methods


def main():
    return


def wrong_letter_match(sorted_input, sorted_word, margin):
    input_index, word_index, wrong_letters, case = 0, 0, [[], []], True
    while True:
        input_letter, word_letter = sorted_input[input_index], sorted_word[word_index]
        if input_letter == word_letter:
            input_index, word_index = input_index + 1, word_index + 1
        elif ord(input_letter) < ord(word_letter):
            if len(wrong_letters[0]) == margin:
                case = False
                break
            wrong_letters[0].append(input_letter)
            input_index += 1
        else:
            if len(wrong_letters[1]) == margin:
                case = False
                break
            wrong_letters[1].append(word_letter)
            word_index += 1
        if input_index == len(sorted_input):
            for index in range(word_index, len(sorted_word)):
                wrong_letters[1].append(sorted_word[word_index])
            break
        if word_index == len(sorted_word):
            for index in range(input_index, len(sorted_input)):
                wrong_letters[0].append(sorted_input[input_index])
            break
    return case, wrong_letters


print(wrong_letter_match("agilnnrs", "aagilmnr", 1))
print(wrong_letter_match("agilnnrs", "aagilmnr", 2))
print(wrong_letter_match("agilnnrs", "aagilmnr", 3))

# TODO Do we run into the same problem as with String_Methods.letter_match when adding the rest of the values in the
#      for loop
