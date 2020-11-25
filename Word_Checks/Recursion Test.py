items = [["Helmet", "Beanie"], ["T-Shirt", "Shirt", "Long-Sleeved Top"], ["Belt"], ["Jeans", "Leggings"],
         ["Trainers", "Sandal's", "Crocs"]]


def recursion(stored_index, index):
    outfit = ""
    for item_index, item_class in enumerate(items):
        outfit += item_class[stored_index[item_index]] + ", "
    print(outfit, stored_index)
    current_index = stored_index[index] + 1
    if current_index != len(items[index]):
        stored_index[index] = current_index
        recursion(stored_index, index)
    else:
        for reverse_index in range(index, -1, -1):
            current_index = stored_index[reverse_index] + 1
            if current_index != len(items[reverse_index]):
                stored_index[reverse_index] = current_index
                recursion(stored_index, index)
                break
            stored_index[reverse_index] = 0
        quit()


recursion([0 for x in range(len(items))], len(items) - 1)










# def recursion(stored_index, index):
#     index += 1
#     if index != len(items):
#         recursion(stored_index, index)
#         current_index = stored_index[index] + 1
#         if current_index != len(items[index]):
#             stored_index[index] = current_index
#             print(stored_index, index)
#             recursion(stored_index, index)
#     else:












    # if index != len(items):
    #
    # else:
    #     current_index = stored_index[index] + 1
    #     if current_index != len(items[index]):
    #         stored_index[index] = current_index
    #     else:

recursion([0, 0, 0, 0, 0], 4)

