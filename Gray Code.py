n = int(input())

for i in range(2**n):
  
  print(str(bin(i^(i>>1))[2:]).rjust(n, '0'))