from collections import deque
import sys
input = sys.stdin.readline

neighbors = [
    [-1,0],
    [0,-1],[0,1],
    [1,0]
  ]
DOT = ord('.')
WALL=ord('#')

def search(si, sj):
  q = deque()
  q.append((si,sj))
  grid[si][sj] = WALL
  while q:
    x,y = q.popleft()
    nx = x-1
    if nx>=0 and grid[nx][y]==DOT:
      grid[nx][y]=WALL
      q.append((nx,y))
    nx=x+1
    if nx<n and grid[nx][y] == DOT:
      grid[nx][y]=WALL
      q.append((nx,y))
    ny=y-1
    if ny>=0 and grid[x][ny]==DOT:
      grid[x][ny]=WALL
      q.append((x,ny))
    ny=y+1
    if ny<m and grid[x][ny]==DOT:
      grid[x][ny]=WALL
      q.append((x,ny))
  

n,m = map(int, input().split())
grid = [bytearray(input().rstrip(), 'ascii') for _ in range(n)]

count = 0
for i in range(n):
  row = grid[i]
  for j in range(m):
    if row[j] == DOT:
      count += 1
      search(i,j)
print(count)