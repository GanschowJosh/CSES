from array import array
import sys
input=sys.stdin.readline
out=sys.stdin.write


n,m=map(int, input().split())
adj=[[] for _ in range(n)]
for _ in range(m):
  a,b=map(int, input().split())
  a-=1;b-=1
  adj[a].append(b)
  adj[b].append(a)

v=bytearray(n)
reps=[]
for i in range(n):
  if v[i]: continue
  reps.append(i)
  stack=[i]
  while stack:
    c=stack.pop()
    for a in adj[c]:
      if v[a]: continue
      v[a]=1
      stack.append(a)

l=len(reps)
print(l-1)
for i in range(l-1):
  print(f"{reps[i]+1} {reps[i+1]+1}")