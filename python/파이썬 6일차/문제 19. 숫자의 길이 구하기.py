def digit_length(n):
    ans = 0
    while n:
        n //= 10
        ans += 1

    return ans
print(digit_length(123))
