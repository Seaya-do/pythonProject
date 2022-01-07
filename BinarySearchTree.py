"""
n 이 41 일때 좌우 대칭으로 배치할 수 있는 트리는 몇 종류인가
"""

N = 41
memory = {0: 1}


def catalan(n):
    if n in memory:
        return memory[n]
    sum = 0
    for i in range(0, n):
        sum += catalan(i) * catalan(n - 1 - i)
    memory[n] = sum
    return sum


if N % 2 == 0:
    print("0")
else:
    print(catalan((N - 1) // 2),"가지")
