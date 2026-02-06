from array import array
from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

n,m = map(int, input().split())

adj = [array('I') for _ in range(n)]

for _ in range(m):
  a,b = map(int, input().split())
  a-=1
  b-=1
  adj[a].append(b)
  adj[b].append(a)

#for i in range(n):
#  print("".join(map(str, adj[i]))+"\n")

vis = bytearray(n)
reps=[]
c=1
q=deque()
for i in range(n):
  if vis[i]: continue
  reps.append(i)
  vis[i]=1
  q.append(i)
  while q:
    curr = q.popleft()
    for v in adj[curr]:
      if not vis[v]:
        vis[v]=1
        q.append(v)
  c+=1

#print("".join(map(str, comps))+"\n")

k = len(reps)
print(str(k-1)+"\n")
for i in range(k-1):
  f = f"{reps[i]+1} {reps[i+1]+1}\n"
  print(f)