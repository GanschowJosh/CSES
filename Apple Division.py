from itertools import combinations
_ = input()
nums = list(map(int, input().split()))
# nums.sort()
s = sum(nums)//2
# print(s)
closest = float('inf')
cl = 0
for i in range(1,len(nums)):
  for c in combinations(nums, i):
    su = sum(c)
    if abs(s-su) < closest:
      closest = abs(s-su)
      cl = su
    # closest = min(closest, abs(s-su))
# print(cl)
print(abs(sum(nums)-cl-cl))