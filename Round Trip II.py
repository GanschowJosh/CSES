from array import array
import sys
input=sys.stdin.readline
out=sys.stdout.write

n,m=map(int, input().split())
adj=[[]for _ in range(n)]
for _ in range(m):
  a,b=map(int, input().split())
  a-=1;b-=1
  adj[a].append(b)


state=[0 for _ in range(n)]#0=unvisited, 1=in stack, 2=done
parent=[-1 for _ in range(n)]

for start in range(n):
  if state[start]!=0:continue

  stack=[(start,0)]
  parent[start]=-1
  state[start]=1

  while stack:
    v,idx=stack[-1]
    if idx==len(adj[v]):
      state[v]=2
      stack.pop()
      continue

    to=adj[v][idx]
    stack[-1]=(v,idx+1)

    # if to==parent[v]:
    #   continue

    if state[to]==0:
      parent[to]=v
      state[to]=1
      stack.append((to,0))
    elif state[to]==1:
      cycle = [to]
      cur=v
      while cur!=to:
        cycle.append(cur)
        cur=parent[cur]
      cycle.append(to)
      cycle.reverse()

      print(len(cycle))
      print(" ".join(str(x+1) for x in cycle))
      exit()

print("IMPOSSIBLE")
