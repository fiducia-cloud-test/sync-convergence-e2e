from itertools import permutations

updates = [('a', 1), ('b', 2), ('c', 3)]

def merge(seq):
    state = ('', -1)
    for value, rev in seq:
        if rev > state[1]:
            state = (value, rev)
    return state

results = {merge(order) for order in permutations(updates)}
assert results == {('c', 3)}
assert merge([('new', 3), ('stale', 2)]) == ('new', 3)
print('formal_wave5_model: ok')
