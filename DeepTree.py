"""
m = 3000, n = 2500일때 2,500번째로 탐색하는 노드의 번호를 구하라.
"""

M, N = 3000, 2500
pre , now, n = 0, 1, N

while n > 1:
    if (pre * 2 == now) or (pre * 2 + 1 == now):
        if now * 2 <= M:
            pre, now, n = now, now * 2, n - 1
        else:
            pre, now = now, now // 2
    else:
        if pre % 2 == 0 :
            if now * 2 + 1 <= M:
                pre, now, n = now, now * 2 + 1, n - 1
            else:
                pre, now = now, now //2
        else:
            pre, now = now, now // 2
print(now,"가지의 방법이 있습니다.")
