# stupid solution
from collections import deque

board = []
for _ in range(8):
  board.append(tuple(input()))
board = tuple(board)

def valid(board):
  out = []
  for i in range(8):
    for j in range(8):
      if board[i][j] not in ['*','q']:
        out.append((i,j))
  return out

def place(board, i, j):
  r = list(map(list, (b for b in board)))
  r[i][j] = 'q'
  for a in range(8):
    if a!=i:r[a][j]='*'
    if a!=j:r[i][a]='*'
  c = 1
  while (i+c)<8 and (j+c)<8: #down right
    if r[i+c][j+c]!='q': r[i+c][j+c]='*'
    c+=1
  c = 1
  while (i-c)>=0 and (j-c)>=0: #up left
    if r[i-c][j-c]!='q': r[i-c][j-c]='*'
    c+=1
  c = 1
  while (i+c)<8 and (j-c)>=0: #down left
    if r[i+c][j-c]!='q': r[i+c][j-c]='*'
    c+=1
  c = 1
  while (i-c)>=0 and (j+c)<8:
    if r[i-c][j+c]!='q': r[i-c][j+c]='*'
    c+=1
  
  return tuple(map(tuple, (b for b in r)))

def count_queens(board):
  c=0
  for i in range(8):
    for j in range(8):
      if board[i][j]=='q':c+=1
  return c

seen = set()
ways = 0
q = deque()
q.append(board)
while q:
  curr = q.popleft()
  if curr in seen:
    continue
  seen.add(curr)
  if count_queens(curr) == 8: ways+=1; continue
  for vr, vc in valid(curr):
    q.append(place(curr, vr, vc))

print(ways)