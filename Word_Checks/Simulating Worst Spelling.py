import itertools


def permutations(word_length, repetition):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    sub_alphabet = tuple(alphabet[1: word_length - repetition + 1])
    positions = list(itertools.combinations([i for i in range(word_length)], repetition))
    for index_set in positions:
        permutation = list(sub_alphabet)
        for index in index_set:
            permutation = permutation[:index] + ["A"] + permutation[index:]
        comparison_type(permutation, word_length)


def comparison_type(permutation, length):
    inverse = permutation[::-1]
    print(permutation, inverse, comparison(length, permutation, inverse))
    swapped = permutation[int(length / 2):] + permutation[:int(length / 2)]
    print(permutation, swapped, comparison(length, permutation, swapped))
    if length % 2 == 0:
        reverse = permutation[int(length / 2):] + permutation[:int(length / 2)]
    else:
        reverse = permutation[int(length / 2) + 1:] + [permutation[int(length / 2)]] \
                  + permutation[:int(length / 2)]
    print(permutation, reverse, comparison(length, permutation, reverse))
    print()


def comparison(length, permutation, to_compare):
    completed, score = [0 for i in range(length)], 0
    for base_index, letter in enumerate(permutation):
        for index, letter_check in enumerate(to_compare):
            if letter_check == letter and completed[index] == 0:
                score += abs(base_index - index)
                completed[index] = 1
                break
    return score


permutations(5, 3)


# if length % 2 == 0:
#     reverse = permutation[int(length / 2):] + permutation[:int(length / 2)]
# else:
#     reverse = permutation[int(length / 2) + 1:] + [permutation[int(length / 2)]] \
#               + permutation[:int(length / 2)]
# print(permutation, reverse, comparison(length, permutation, reverse))
# Unnecessary - Never produces the greatest value


