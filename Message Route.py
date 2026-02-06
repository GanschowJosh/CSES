from collections import deque
n, m = map(int, input().split())
INF = 10**18

def bfs(n, adj, s):
  dist = [INF]*(n+1)
  parent = [-1]*(n+1)

  q = deque({s})
  dist[s]=0
  while q:
    c = q.popleft()
    for a in adj[c]:
      if dist[a] != INF: continue
      dist[a]=dist[c]+1
      parent[a]=c
      q.append(a)

  return dist, parent

def get_path(parent, s):
  p = []
  c = s
  while c != -1:
    p.append(c)
    c = parent[c]
  p.reverse()
  return p

adj = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int, input().split())
  adj[a].append(b)
  adj[b].append(a)

dist, parent = bfs(n, adj, 1)
if dist[n]==INF: print("IMPOSSIBLE"); exit()
print(dist[n]+1)
p = get_path(parent, n)
for a in range(len(p)-1):
  print(p[a], end=" ")
print(p[-1])