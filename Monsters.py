from collections import deque
from array import array
import sys
input = sys.stdin.readline
out = sys.stdout.write

INF = 10**9
dirs = [(-1,0,'U'), (1,0,'D'), (0,-1,'L'), (0,1,'R')]
A=ord('A')
M=ord('M')
WALL=ord('#')

n,m = map(int, input().split())
gr = []
midx = []
for _ in range(n):
  line = bytearray(input().strip(),'ascii')
  if A in line: aloc=(_, line.index(A))
  midx.extend(list((_,i) for i,x in enumerate(line) if x==M))
  gr.append(line)

mon_time = [[-1]*m for _ in range(n)]
for i in range(n):
  for j in range(m):
    if gr[i][j]==WALL:
      mon_time[i][j]=INF
q = deque() #r,c,time
for mx,my in midx:
  q.append((mx,my,0))
  mon_time[mx][my]=0

while q:
  cx,cy,ct=q.popleft()
  for dx,dy,_ in dirs:
    nx,ny=cx+dx,cy+dy
    if 0>nx or nx>=n or 0>ny or ny>=m or mon_time[nx][ny]!=-1:continue
    mon_time[nx][ny]=ct+1
    q.append((nx,ny,ct+1))

q=deque([(aloc[0],aloc[1],0)])#x,y,time
v=[bytearray(m) for _ in range(n)]
v[aloc[0]][aloc[1]]=1
par=[bytearray(m) for _ in range(n)] #u,l,d,r = 0,1,2,3
par[aloc[0]][aloc[1]]=0
end=None
if aloc[0] == 0 or aloc[0] == n - 1 or aloc[1] == 0 or aloc[1] == m - 1:
  end = (aloc[0], aloc[1])
while q and end is None:
  cx,cy,ct=q.popleft()
  # print(cx,cy,ct)
  if cx==0 or cx==n-1 or cy==0 or cy==m-1:end=(cx,cy);q.clear();break
  for k, (dx,dy,_) in enumerate(dirs):
    nx,ny=cx+dx,cy+dy
    # print(nx,ny)
    mt=mon_time[nx][ny]
    if 0>nx or nx>=n or 0>ny or ny>=m or v[nx][ny]!=0 or gr[nx][ny]==WALL or (mt!=-1 and mt<=ct+1):continue
    v[nx][ny]=1
    par[nx][ny]=k
    q.append((nx,ny,ct+1))
if end is None:
  print("NO")
  exit()

path = []
x,y=end
dirmap={
  (-1,0):'D',
  (0,-1):'R',
  (0,1):'L',
  (1,0):'U'
}
while (x,y) != (aloc[0],aloc[1]):
  k=par[x][y]
  dx,dy,c=dirs[k]
  path.append(c)
  x-=dx
  y-=dy
path.reverse()
print("YES")
print(len(path))
out("".join(path))
out("\n")