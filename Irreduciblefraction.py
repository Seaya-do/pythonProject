"""
분모와 분자의 합이 1,234,567이 되는 0과 1 사이에 있는 기약 분수가 몇 개인지 구하라.
"""
from fractions import gcd

Num = 1234567
cnt = 0

for i in range(1, Num // 2 + 1):
    if gcd(i, Num - i) == 1:
        cnt += 1

print(cnt)
