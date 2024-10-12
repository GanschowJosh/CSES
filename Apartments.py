n, m, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
curra = 0
b = sorted(list(map(int, input().split())))
currb = 0
placed = 0
while currb < m and curra < n:
    if a[curra] < b[currb] - k:
        #apartment too small, move to next apartment
        curra+=1
    elif a[curra] > b[currb] + k:
        #apartment too large, move to next applicant
        currb += 1
    else:
        #apartment acceptable
        placed += 1
        curra += 1
        currb += 1

print(placed)
