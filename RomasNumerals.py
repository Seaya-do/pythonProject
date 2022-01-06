"""
로마 숫자 기호를 12개 나열했을 때, 로마 숫자로 인식될 수 있는 숫자가 몇 개인지 구하시오.
"""


N = 12

# 자릿수 변환
def conv(n, i, v, x):
    result = ''
    if n == 9:
        result += i + x
    elif n == 4:
        result += i + v
    else:
        result += v * (n // 5)
        n = n % 5
        result += i * n
    return result

# 로마숫자 변환
def roman(n):
    m, n = divmod(n, 1000)
    c, n = divmod(n, 100)
    x, n = divmod(n, 10)
    result = 'M' * m
    result += conv(c, 'C', 'D', 'M')
    result += conv(x, 'X', 'L', 'C')
    result += conv(n, 'I', 'V', 'X')
    return result


cnt = {}
for n in range(1, 4000):
    length = len(roman(n))
    if length in cnt:
        cnt[length] += 1
    else:
        cnt[length] = 1
print(cnt[N] ,'개')

