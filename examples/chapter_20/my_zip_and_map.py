"""
Chapter 20: Comprehensions and Generations
My map and zip functions

- my_map1 - returns list
- my_map2 - returns list with list comprehension
- my_map3 - returns generator with yield statement
- my_map4 - returns generator with comprehension
"""

#
# def my_map1(func, *seqs):
#     res = []
#     for args in zip(*seqs):
#         res.append(func(*args))
#     return res
#
#
# def my_map2(func, *seqs):
#     return [func(*args) for args in zip(*seqs)]
#
#
# print(my_map1(abs, [-1, 2, 3]))
# print(my_map1(pow, [1, 2, 3], [2, 3, 4]))
# print(my_map2(abs, [-1, 2, 3]))
# print(my_map2(pow, [1, 2, 3], [2, 3, 4]))
#
#
# def my_map3(func, *seqs):
#     for args in zip(*seqs):
#         yield func(*args)
#
#
# def my_map4(func, *seqs):
#     return (func(*args) for args in zip(*seqs))
#
#
# print(my_map3(abs, [-1, 2, 3]))
# map3 = my_map3(pow, [1, 2, 3], [2, 3, 4])
# print(my_map4(abs, [-1, 2, 3]))
# map4 = my_map4(pow, [1, 2, 3], [2, 3, 4])
#
#
# while True:
#     try:
#         print(next(map4))
#     except StopIteration:
#         print("Iterator exhausted")
#         break


def my_zip1(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res


def my_zip2(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)


def my_zip3(*seqs):
    minlen = min([len(S) for S in seqs])
    return [tuple(S[i] for S in seqs) for i in range(minlen)]


S1 = "abcf"
S2 = "xyz123"
print(my_zip3(S2, S1))


def my_map_pad1(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res


def my_map_pad2(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)


def my_map_pad3(*seqs, pad=None):
    maxlen = max([len(S) for S in seqs])
    index = range(maxlen)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]


print(my_map_pad1(S2, S1))
print(my_map_pad1(S2, S1, pad=99))
print(my_map_pad2(S2, S1))
print(my_map_pad3(S2, S1))
