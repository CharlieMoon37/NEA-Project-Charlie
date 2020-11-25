import os
import time


def main():
    path = os.getcwd().replace("Word_Checks", "Sorted_Lists")
    os.chdir(path)
    function_start = time.time()
    for num in range(1, 32):
        try:
            with open(str(num) + " Letters.txt", "r") as word_file:
                file_start = time.time()
                for line in word_file:
                    char_list = []
                    for char in line[:-1]:
                        char_list.append(char)
                    char_list.sort()
                    sorted_letters = ""
                    for char in char_list:
                        sorted_letters += char
                file_end = time.time()
                print(str(num) + ":", file_end - file_start)
        except FileNotFoundError:
            continue
    function_end = time.time()
    print("Total Time: " + str(function_end - function_start))


main()








