import os
import time


def main(word):
    word = word.lower()  # All dictionary entries are lowercase
    path = os.getcwd().replace("Word_Checks", "Sorted_Lists")
    os.chdir(path)  # Selects the correct directory
    with open(str(len(word)) + " Letters.txt") as word_file:
        start = time.time()
        for index, line in enumerate(word_file):
            if line[0:-1] == word:  # Takes the last character ("\n") off
                end = time.time()
                print(index, (end - start))  # Returns the file index and search time
                break


main("Zymolytic")






