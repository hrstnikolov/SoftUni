def get_indices(ll, value):
    indices = []
    index = 0
    while True:
        try:
            new_index = ll.index(value, index)
            indices.append(index)
            index = new_index + 1
        except ValueError:
            break
    return indices