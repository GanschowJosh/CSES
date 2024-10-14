n = int(input())
for i in range(1, n+1):
    allPossible = i*i*(i*i-1)*0.5
    attackingArrangements = 4*(i-1)*(i-2)
    print(int(allPossible-attackingArrangements))
