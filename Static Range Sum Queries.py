n, q = map(int, input().split())
nums = list(map(int, input().split()))
pref = [0]*n
pref[0] = nums[0]
for i in range(1, n):
  pref[i] = pref[i-1]+nums[i]

s = lambda x, y: pref[y]-(pref[x-1] if x>=1 else 0)

ans = []

for _ in range(q):
  a, b = map(int, input().split())
  ans.append(str(s(a-1,b-1)))

print("\n".join(ans))