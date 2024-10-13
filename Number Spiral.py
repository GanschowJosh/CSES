def find(y, x):
    if y>x:
        if y%2:
            return x+(y-1)*(y-1)
        else:
            return (2*y-x)+(y-1)*(y-1)
    else:
        if x%2:
            return (2*x-y)+(x-1)*(x-1)
        else:
            return y+(x-1)*(x-1)
t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    print(find(y, x))