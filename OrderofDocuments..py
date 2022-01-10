"""
문서가 15개 있을 때 책장에 들어 있을 수 있는 문서의 배치 패턴을 모두 생각하고, 원래 순서로 되돌리는 이동 횟수의 합계를 구하라.
"""

N = 15
cnt = [0] * N
cnt[0] = 1
for i in range(1, N + 1):
    for j in range(0, i - 2):
        cnt[i - j - 1] = cnt[i - j - 2] * i
    cnt[1] = i - 1

sum = 0
for v, i in enumerate(cnt):
    sum += i * v
print(sum, "번")