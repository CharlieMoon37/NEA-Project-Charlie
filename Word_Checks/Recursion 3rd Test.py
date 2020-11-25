item_set = [[2, ["T-Shirt", "Jumper", "Coat", "Scarf"]], [1, ["Jeans", "Leggings"]],
            [1, ["Trainers", "Sandal's", "Crocs"]]]

items = [["T-Shirt", "Jumper", "Coat", "Scarf"], ["T-Shirt", "Jumper", "Coat", "Scarf"],
         ["Jeans", "Leggings"], ["Trainers", "Sandal's", "Crocs"]]


def startup():
    stored_index = []
    for item in item_set:
        for x in range(0, item[0]):
            stored_index.append(x)
    recursion(tuple(stored_index), stored_index)


def recursion(base, stored_index):
    # outfit = ""
    # for item_index, item_class in enumerate(items):
    #     outfit += item_class[stored_index[item_index]] + ", "
    # print(outfit)
    # ----------------------------------------------------------
    print(stored_index)
    for reverse_index in range(len(items) - 1, -1, -1):
        current_index = stored_index[reverse_index] + 1
        if current_index != len(items[reverse_index]):
            if base[reverse_index + 1] != 0:
                group_start, group_count = reverse_index, 1
                while base[reverse_index + 1] != 0:
                    group_count += 1
                    reverse_index += 1
                if stored_index[group_start] + group_count < len(items[group_start]):
                    current_value = stored_index[group_start]
                    for index in range(group_start, reverse_index + 1):
                        current_value += 1
                        stored_index[index] = current_value
                    recursion(base, stored_index)
                    break
            else:
                stored_index[reverse_index] = current_index
                recursion(base, stored_index)
                break
        stored_index[reverse_index] = 0
    quit()


startup()
