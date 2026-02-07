from collections import deque
from array import array
import sys
input = sys.stdin.readline
out = sys.stdout.write

n,m=map(int, input().split())

adj = [array('I') for _ in range(n)]
for _ in range(m):
  a,b=map(int, input().split())
  a-=1;b-=1
  adj[a].append(b)
  adj[b].append(a)

reps=[]
v=bytearray(n)
for i in range(n):
  if v[i]==1:continue
  reps.append(i)
  q = deque([i])
  v[i]=1
  while q:
    c=q.popleft()
    for a in adj[c]:
      if v[a]!=1:
        q.append(a)
        v[a]=1
l=len(reps)
print(l-1)
for i in range(l-1):
  print(f"{reps[i]+1} {reps[i+1]+1}")
