# from collections import deque
# n = int(input())

# t = [
#   (0,1),
#   (0,2),
#   (1,2),
#   (1,0),
#   (2,0),
#   (2,1)
# ]

# def nxt(s):
#   ss = []
#   for a,b in t:
#     ns = list(map(list, s))
#     if not ns[a]: continue
#     if ns[b] and not ns[a][-1] < ns[b][-1]: continue
#     ns[b].append(ns[a].pop(-1))
#     ss.append((tuple(map(tuple, ns)), (a,b)))
#   return tuple(ss)

# def reconstruct(parent, curr):
#   c = 0
#   out = []
#   while curr[1] != None:
#     a, b = curr[1][0]+1, curr[1][1]+1
#     out.append(" ".join(map(str, (a,b))))
#     curr = parent[curr]
#     c += 1
#   print(c)
#   print("\n".join(reversed(out)))

# st = (tuple(reversed(range(1, n+1))), tuple(), tuple())
# targ = (tuple(),tuple(),tuple(reversed(range(1, n+1))))
# q = deque([(st, None)])
# visited = {st}
# parent = {(st,None): None}
# while q:
#   curr = q.popleft()
#   state, _ = curr
#   # print(curr)
#   if state == targ: reconstruct(parent, curr); break
#   for ns, nv in nxt(state):
#     if ns in visited: continue
#     visited.add(ns)
#     node=(ns,nv)
#     parent[node]=curr
#     q.append(node)

# recursive soln
def tow(n, f, t, a):
  if n == 0: return 
  tow(n-1,f,a,t)
  print(f"{f} {t}")
  tow(n-1,a,t,f)

n = int(input())
print(2**n-1)
tow(n, "1", "3", "2")