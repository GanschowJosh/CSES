n = int(input())
inl = list(map(int, input().split())) #input list
totalSum = (n*(n+1))//2

givenSum = sum(inl)
print(totalSum-givenSum)

