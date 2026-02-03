from itertools import permutations
from math import factorial
s = list(input())
# print(factorial(len(s)))
out = set()
# s.sort()
for p in permutations(s):
  out.add("".join(p))
print(len(out))
out = list(out)
out.sort()
print("\n".join(out))