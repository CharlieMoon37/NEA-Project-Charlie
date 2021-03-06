import itertools


def ordered_permutations(word_length, repetition):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    sub_alphabet = tuple(alphabet[1: word_length - repetition + 1])
    permutations = list(itertools.permutations(["A"] * repetition + list(sub_alphabet)))
    positions = list(itertools.combinations([i for i in range(word_length)], repetition))
    for index_set in positions:
        current_permutation = list(sub_alphabet)
        for index in index_set:
            current_permutation = current_permutation[:index] + ["A"] + current_permutation[index:]
        worst_permutations, highest_score = [], 0
        for permutation in permutations:
            score = comparison(word_length, current_permutation, permutation)
            if score > highest_score:
                highest_score, worst_permutations = score, [permutation]
            elif score == highest_score:
                worst_permutations.append(permutation)
        print("Current Permutation:", current_permutation)
        print("Worst Score:", highest_score)
        print("Worst Permutations:")
        print(set(worst_permutations))
        print()
        comparison_methods(current_permutation, word_length, highest_score, len(set(worst_permutations)))


def comparison_methods(permutation, length, highest_score, possibilities):
    case = False
    inverse = permutation[::-1]
    if comparison(length, permutation, inverse) == highest_score:
        print("Inverse (" + str(inverse) + ") is 1 of " + str(possibilities) + " Worst Permutations of " + str(permutation))
        case = True
    swapped = permutation[int(length / 2):] + permutation[:int(length / 2)]
    if comparison(length, permutation, swapped) == highest_score:
        print("Swapped (" + str(swapped) + ") is 1 of " + str(possibilities) + " Worst Permutations of " + str(permutation))
        case = True
    if length % 2 != 0:
        reverse = permutation[int(length / 2) + 1:] + [permutation[int(length / 2)]] \
                  + permutation[:int(length / 2)]
        if comparison(length, permutation, reverse) == highest_score:
            print("Reverse (" + str(reverse) + ") is 1 of " + str(possibilities) + " Worst Permutations of " + str(permutation))
            case = True
    if not case:
        print("Error: Current Methods are Invalid for All " + str(possibilities) + " Worst Permutations of " + str(permutation))
    print("\n" * 2)


def comparison(length, permutation, to_compare):
    completed, score = [0 for i in range(length)], 0
    for base_index, letter in enumerate(permutation):
        for index, letter_check in enumerate(to_compare):
            if letter_check == letter and completed[index] == 0:
                score += abs(base_index - index)
                completed[index] = 1
                break
    return score


ordered_permutations(5, 3)
