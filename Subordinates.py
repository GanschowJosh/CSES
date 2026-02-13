from array import array
import sys
input=sys.stdin.readline
out=sys.stdout.write

n=int(input().strip())
par=list(map(int, input().split()))

children=[[] for _ in range(n)]
for i in range(1,n):
  p=par[i-1]-1
  children[p].append(i)

order=[]
s=[0]
while s:
  v=s.pop()
  order.append(v)
  for c in children[v]:
    s.append(c)

sub=[1]*n
for v in reversed(order):
  for c in children[v]:
    sub[v]+=sub[c]

print(" ".join(str(sub[i]-1) for i in range(n)))