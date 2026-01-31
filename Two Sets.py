n = int(input())
if not (n%4==0 or (n+1)%4==0): print("NO"); exit()

print("YES")
t = n*(n+1)/4
a = set(range(1, n+1))
inc = set()
while n >= 1:
  if t-n >= 0: inc.add(n);t-=n
  elif t == 0: break
  n -= 1

ot = a-inc
print(len(inc))
print(" ".join(map(str, inc)))
print(len(ot))
print(" ".join(map(str, ot)))
