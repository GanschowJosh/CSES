from array import array
import sys
input=sys.stdin.readline
out=sys.stdout.write

n,m=map(int,input().split())
adj=[set() for _ in range(n)]
for _ in range(m):
  a,b=map(int, input().split())
  a-=1;b-=1
  adj[a].add(b)
  adj[b].add(a)

team=bytearray(n)
for s in range(n):
  if team[s]:continue
  team[s]=1
  stack=[s]
  while stack:
    v=stack.pop()
    for u in adj[v]:
      if not team[u]:
        team[u]=1 if team[v]==2 else 2
        stack.append(u)
      elif team[u]==team[v]:print("IMPOSSIBLE");exit()

for i in team:
  print(i, end=" ")