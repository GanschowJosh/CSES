"""tle approach
n = int(input())
l = list(map(int, input().split()))
print(len(set(l)))
"""
#stupid question, not even an algorithm problem, just figuring out how to read stdin faster
import sys
n = int(input())
input = sys.stdin.read
data = input().split()

print(len(set(data)))