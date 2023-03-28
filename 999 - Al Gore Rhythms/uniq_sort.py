unsorted = [4, 2, 2, 3, 2, 2, 2, 1, 5]


def uniq_sort(array, reverse=False):
    """remove dupl, return sorted list"""
    holder = []

    for value in array:
        if value not in holder:
            holder.append(value)

    return sorted(holder, reverse=reverse)


print(uniq_sort(unsorted, True))
