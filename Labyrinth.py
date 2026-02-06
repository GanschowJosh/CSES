from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

DOT = ord('.')
WALL = ord('#')
A = ord('A')
B = ord('B')


def search(si, sj):
  q = deque()
  bi,bj = bloc
  q.append((si,sj))
  g = gr
  par = [bytearray(m) for _ in range(n)]
  par[si][sj]=1
  while q:
    i,j = q.popleft()
    if i == bi and j == bj:
      break
    ni = i-1
    if ni>=0 and g[ni][j]!=WALL and par[ni][j]==0:
      par[ni][j]=ord('U')
      q.append((ni,j))
    ni=i+1
    if ni<n and g[ni][j]!=WALL and par[ni][j]==0:
      par[ni][j]=ord('D')
      q.append((ni,j))
    nj=j-1
    if nj>=0 and g[i][nj]!=WALL and par[i][nj]==0:
      par[i][nj]=ord('L')
      q.append((i,nj))
    nj=j+1
    if nj<m and g[i][nj]!=WALL and par[i][nj]==0:
      par[i][nj]=ord('R')
      q.append((i,nj))
  return par

def reconstruct(par):
  p = []
  i,j = bloc
  si,sj=aloc
  while not (i==si and j==sj):
    d = par[i][j]
    p.append(chr(d))
    if d==ord('U'):i+=1
    elif d==ord('D'):i-=1
    elif d==ord('L'):j+=1
    else: j-=1
  p.reverse()
  return p


n, m = map(int, input().split())
gr = []
aloc = None
bloc = None
for _ in range(n):
  r = bytearray(input().rstrip(),'ascii')
  if A in r:
    aloc = (_, r.index(A))
  if B in r:
    bloc = (_, r.index(B))
  gr.append(r)

par = search(aloc[0],aloc[1])
if par[bloc[0]][bloc[1]]==0:print("NO\n"); exit()
path = reconstruct(par)
print("YES\n")
print(str(len(path))+"\n")
print("".join(path)+"\n")
