import math
n = int(input())
out = 0
for i in range(1, int(math.log(n, 5))+1):
    out += math.floor(n/math.pow(5, i))
print(out)