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
        print(current_permutation, highest_score)


def comparison(length, permutation, to_compare):
    completed, score = [0 for i in range(length)], 0
    for base_index, letter in enumerate(permutation):
        for index, letter_check in enumerate(to_compare):
            if letter_check == letter and completed[index] == 0:
                score += abs(base_index - index)
                completed[index] = 1
                break
    return score


ordered_permutations(6, 3)












