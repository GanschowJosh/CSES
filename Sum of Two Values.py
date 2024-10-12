"""from collections import defaultdict

n, x = map(int, input().split())
nums = list(map(int, input().split()))

d = defaultdict(list)
out = False
for i in range(n):
    complement = x-nums[i]
    if complement in d:
        print(f"{d[complement] + 1} {i+1}")
        out = True
        break
    d[nums[i]] = i
if not out:
    print("IMPOSSIBLE")
    """
"""
import sys
input = sys.stdin.read
data= input().split()

n= int(data[0])
x = int(data[1])
nums = list(map(int, data[2:n+2]))

d = {}
out = False
for i in range(n):
    complement = x-nums[i]
    if complement in d:
        sys.stdout.write(f"{d[complement] + 1} {i+1}\n")
        out = True
        break
    d[nums[i]] = i
if not out:
    sys.stdout.write("IMPOSSIBLE\n")
    """
#solution: repeatedly move left pointer and right pointer closer together until sum found or not
n, x = map(int, input().split())
nums = list(map(int, input().split()))

# Store original indices before sorting
nums_with_indices = [(nums[i], i + 1) for i in range(n)]
nums_with_indices.sort()

left, right = 0, n - 1
out = False

while left < right:
    current_sum = nums_with_indices[left][0] + nums_with_indices[right][0]
    
    if current_sum == x:
        print(f"{nums_with_indices[left][1]} {nums_with_indices[right][1]}")
        out = True
        break
    elif current_sum < x:
        left += 1
    else:
        right -= 1

if not out:
    print("IMPOSSIBLE")
