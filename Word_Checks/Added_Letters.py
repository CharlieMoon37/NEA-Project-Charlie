import os
import time
from Word_Checks import String_Methods


def main(char_input, margin):
    os.chdir(os.getcwd().replace("Word_Checks", "Sorted_Lists"))
    sorted_long_string, long_string = String_Methods.letter_sort(char_input)[0], char_input
    with open(str(len(char_input) - margin) + " Letters.txt", "r") as word_file:
        for line in word_file:
            sorted_short_string, short_string = String_Methods.letter_sort(line[:-1])[0], line[:-1]
            case, extra_letters, extra_letter_set = \
                String_Methods.letter_match(sorted_long_string, margin, sorted_short_string)
            if case:
                extra_letter_indexes = String_Methods.get_letter_indexes(long_string, extra_letter_set, extra_letters)
                index_store, letter_indexes = String_Methods.recursion_setup(extra_letter_indexes)
                String_Methods.recursion(tuple(index_store), index_store, letter_indexes, long_string, short_string)


total_time = 0
for x in range(20):
    start = time.time()
    main("copmmmputrer", 4)
    main("afriednd", 2)
    main("alalarmiing", 3)
    main("remijnsded", 2)
    main("preeerfectly", 3)
    end = time.time()
    total_time += (end - start)
print(total_time / 20)


# TODO Use a trie???
# main("cohenrenyt", 2)
# main("requiremenet", 1)
# main("aupmple", 2)
# main("wouklld", 2)
# main("wmatserr", 2)
# main("hgoood", 2)
# main("copoyistst", 2)
# main("alalarmiing", 3)
# main("duiinner", 2)
# main("ehoerrible", 2)
# main("wewell", 2)
# main("alarmining", 2)
# main("ioutliying", 2)
# main("secdonbd", 2)
# main("nwihcih", 2)
# main("reatsrt", 0)
# main("wha", -1)
# main("uroa", -2)
# main("alrming", -1)
# main("reuirment", -2)
# main("kenw", 0)
# main("gnight", 1)
# main("qween", -1)
