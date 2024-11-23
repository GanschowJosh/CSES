t = int(input())
results = []

for _ in range(t):
    a, b = map(int, input().split())
    if (a + b) % 3 == 0 and 2 * min(a, b) >= max(a, b):
        results.append("YES")
    else:
        results.append("NO")

for result in results:
    print(result)

