# Get a life Charlie

# def main(word, extras):
#     os.chdir(os.getcwd().replace("Word_Checks", "Sorted_Lists"))
#     sorted_word = letter_sort(word)
#     with open(str(len(word) - extras) + " Letters.txt", "r") as word_file:
#         for line in word_file:
#             case = True
#             sorted_letters = letter_sort(line[:-1])
#             added = 0
#             for index, letter in enumerate(sorted_letters):
#                 if letter != sorted_word[index + added]:
#                     if extras == 0:
#                         case = False
#                         break
#                     extras, added = extras - 1, added + 1
#             if case:
#                 print(line[:-1], sorted_letters, word, sorted_word)

# def input_permutations(char_input, extra_letters_set):
#     print(extra_letters_set)
#     extra_letter_indexes = []
#     for extra_letter, letter_count in extra_letters_set:
#         letter_indexes = []
#         for index, letter in enumerate(char_input):
#             if letter == extra_letter:
#                 letter_indexes.append(index)
#         if len(letter_indexes) > letter_count:
#             extra_letter_indexes.append([letter_count, letter_indexes])
#         else:
#             char_input = char_input.replace(extra_letter, "")
#     return extra_letter_indexes, char_input


# def percent_match(char_input, suggested, extra_letters):
#     removed, char_list = 0, list(char_input)
#     # print(char_list)
#     for extra_letter in extra_letters:
#         char_list.pop(extra_letter[1] - removed)
#         removed += 1
#         # print(char_list)
#     print("".join(char_list), extra_letters)  # TODO Scrapbook?
