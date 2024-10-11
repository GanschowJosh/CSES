s = input()
curr = 1
max = 1
last = s[0]
for i in range(1, len(s)):
    if s[i] == last:
        curr += 1
        if curr > max:
            max = curr
    else:
        curr = 1
    last = s[i]
print(max)