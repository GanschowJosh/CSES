def number_up_to_n_digits(n):
    if n <= 0:
        return -1
    
    digits = 1
    count = 9
    start = 1
    while n > digits*count:
        n -= digits * count
        digits += 1
        count *= 10
        start *= 10

    number = start + (n-1) // digits
    digit_idx = (n-1) % digits
    return int(str(number)[digit_idx])

q = int(input())
for _ in range(q):
    curr_num = int(input())
    print(number_up_to_n_digits(curr_num))
