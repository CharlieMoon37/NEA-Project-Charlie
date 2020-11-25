item_set = [[3, ["T-Shirt", "Jumper", "Coat", "Scarf", "Hat"]], [2, ["Jeans", "Leggings"]],
            [1, ["Trainers", "Sandal's", "Crocs"]]]

items = [["T-Shirt", "Jumper", "Coat", "Scarf", "Hat"], ["T-Shirt", "Jumper", "Coat", "Scarf", "Hat"],
         ["T-Shirt", "Jumper", "Coat", "Scarf", "Hat"], ["Jeans", "Leggings"], ["Jeans", "Leggings"],
         ["Trainers", "Sandal's", "Crocs"]]


def startup():
    index_store = []
    for item in item_set:
        for r in range(0, item[0]):
            index_store.append(r)
    index_store.append(0)
    recursion(tuple(index_store), index_store)


def recursion(base, index_store):
    # outfit = ""
    # for item_index, item_class in enumerate(items):
    #     outfit += item_class[index_store[item_index]] + ", "
    # print(outfit)
    # ----------------------------------------------------------
    print(index_store[:-1])
    for index in range(len(base) - 2, -1, -1):
        current_value, n = index_store[index], len(items[index])
        next_value = current_value + 1
        if next_value < n:
            if base[index + 1] == 0:
                index_store[index] = next_value
                recursion(base, index_store)
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
                    recursion(base, index_store)
                    break
        index_store[index] = 0


startup()

















