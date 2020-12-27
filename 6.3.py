n = 1234
sum = 0
while n > 0:
    digit = n%10
    print(digit)
    sum +=digit
    print(sum)
    n //=10
    print(n)
print('끝')
print(sum)
