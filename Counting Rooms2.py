from array import array
import sys
input=sys.stdin.readline
out=sys.stdout.write

DOT=ord('.')
WALL=ord('#')

dirs=((-1,0),(1,0),(0,-1),(0,1))

n,m=map(int, input().split())
gr=[bytearray(input().strip(),'ascii')for _ in range(n)]

found=0
for i in range(n):
  for j in range(m):
    c=gr[i][j]
    if c!=DOT:continue
    found+=1
    gr[i][j]=WALL
    stack=[(i,j)]
    while stack:
      cx,cy=stack.pop()
      for dx,dy in dirs:
        nx,ny=dx+cx,dy+cy
        if 0>nx or n<=nx or 0>ny or m<=ny:continue
        if gr[nx][ny]!=DOT:continue
        gr[nx][ny]=WALL
        stack.append((nx,ny))

print(found)
