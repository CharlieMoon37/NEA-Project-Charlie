def letter_sort(word):
    char_list = []
    for char in word:
        char_list.append(char)
    char_list.sort()
    sorted_letters = ""
    for char in char_list:
        sorted_letters += char
    return sorted_letters, char_list


def letter_match(sorted_long_string, margin, sorted_short_string):
    extra_letters, extra_letter_set = [], []
    for index, letter in enumerate(sorted_long_string):
        if index - len(extra_letters) == len(sorted_short_string):
            for letter_index in range(index, len(sorted_long_string)):
                extra_letters, extra_letter_set = \
                    update_extra_letter_stores(extra_letters, extra_letter_set, sorted_long_string[letter_index])
                # TODO Do I need to check again if the list exceeds the margin???
            break
        if letter != sorted_short_string[index - len(extra_letters)]:
            if len(extra_letters) == margin:
                return False, 0, 0
            extra_letters, extra_letter_set = \
                update_extra_letter_stores(extra_letters, extra_letter_set, letter)
            # TODO Could this be a list comparison popping each value in the list if it matches
            #      Would it be more efficient?
    return True, extra_letters, extra_letter_set


def update_extra_letter_stores(extra_letters, extra_letter_set, letter):
    extra_letters.append(letter)
    case = True
    for set_index, letter_set in enumerate(extra_letter_set):
        if letter_set[0] == letter:
            extra_letter_set[set_index][1] += 1
            case = False
            break
    if case:
        extra_letter_set.append([letter, 1])
    return extra_letters, extra_letter_set


def get_letter_indexes(long_string, extra_letter_set, extra_letters):
    extra_letter_indexes = [[extra_letter, [], count] for [extra_letter, count] in extra_letter_set]
    for input_index, input_letter in enumerate(long_string):
        if input_letter in set(extra_letters):
            for index, letter_indexes in enumerate(extra_letter_indexes):
                if letter_indexes[0] == input_letter:
                    extra_letter_indexes[index][1].append(input_index)
                    break
    return extra_letter_indexes


def recursion_setup(extra_letter_indexes):
    index_store, letter_indexes = [], []
    for item in extra_letter_indexes:
        for r in range(0, item[2]):
            index_store.append(r)
            letter_indexes.append(item[1])
    index_store.append(0)
    return index_store, letter_indexes


def recursion(base, index_store, letter_indexes, long_string, short_string):
    items_to_remove = []
    for item_index, item_class in enumerate(letter_indexes):
        items_to_remove.append(item_class[index_store[item_index]])
    comparison(long_string, sorted(items_to_remove), short_string)
    # ----------------------------------------------------------
    for index in range(len(base) - 2, -1, -1):
        current_value, n = index_store[index], len(letter_indexes[index])
        next_value = current_value + 1
        if next_value < n:
            if base[index + 1] == 0:
                index_store[index] = next_value
                recursion(base, index_store, letter_indexes, long_string, short_string)
                break
            else:
                group_index = index + 2
                while base[group_index] != 0:
                    group_index += 1
                group_length = group_index - index
                if current_value + group_length < n:
                    for update_index in range(index, group_index):
                        index_store[update_index] = next_value
                        next_value += 1
                    recursion(base, index_store, letter_indexes, long_string, short_string)
                    break
        index_store[index:] = base[index:]


def comparison(long_string, items_to_remove, short_string):
    for index, item in enumerate(items_to_remove):
        long_string = long_string[:item - index] + long_string[item - index + 1:]
    completed, score = [0 for i in range(len(short_string))], 0
    for base_index, letter in enumerate(short_string):
        for index, letter_check in enumerate(long_string):
            if letter_check == letter and completed[index] == 0:
                score += abs(base_index - index)
                completed[index] = 1
                break
    print(long_string, short_string, score)
    return score
