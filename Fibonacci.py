import re

a = b = 1
count = 0

while count < 11:
    c = a + b
    # 1자리씩 나눠서 각 자리의 합을 구함
    sum = 0
    for d in str(c):
        sum += int(d)
    if c % sum == 0:
        # 나누어서 떨어지면 출력
        print(c)
        count += 1
    a, b = b, c


