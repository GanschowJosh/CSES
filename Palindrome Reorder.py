from collections import Counter
import sys
input = sys.stdin.readline

s = input().strip()

c = Counter(s)
if not all(val%2==0 for val in c.values()) and not len([val for val in c.values() if val%2==1]) == 1:
  print("NO SOLUTION")
  exit()

left = []
mid = ""
for ch, cnt in c.items():
  left.append(ch*(cnt//2))
  if cnt%2==1: mid=ch

left = "".join(left)
res = left+mid+left[::-1]
print(res)