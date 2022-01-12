"""

원주율과 가까운 분수 중 n = 11일때 pi(11)의 분모를 구하라.
"""
from math import floor

N = 11
q = 1

pi = int("314159265358"[0:N + 1])
pow = 10 ** N

while True:
    if floor(q * pi / pow) != floor(q * (pi + 1) / pow):
        if q * (pi + 1) % pow > 0:
            print(q)
            break
    q += 1
