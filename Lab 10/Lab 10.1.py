B = [5, -3, -2, 3, 2, -7, 1]
print('Початковий список:',B)

def form_new_list(B):

    is_decreasing = all(B[i] > B[i + 1] for i in range(len(B) - 1))
    if is_decreasing:
        return B.copy()

    return [1 if x < 0 else x for x in B]

new_list = form_new_list(B)
print("Новий список:     ", new_list)
