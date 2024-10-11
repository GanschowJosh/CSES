n = int(input())
inp = list(map(int, input().split()))

moves = 0
last = inp[0]
for i in range(1, len(inp)):
    if last > inp[i]:
        moves += (last-inp[i])
        inp[i] = last
    last = inp[i]

print(moves)