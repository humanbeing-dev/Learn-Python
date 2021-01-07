import math
from permute import permute1, permute2

math.factorial(10)

seq = list(range(10))
# p1 = permute1(seq)
# print(len(p1), p1[0], p1[1])

p2 = permute2(seq)

print(next(p2))
print(next(p2))