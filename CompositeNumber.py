"""
합성수란 1과 그 수 자신 이외의 약수를 가지는 자연수
문)1~N의 합성수에서 7개 수를 골랐을 때 최대 6단계를 거치게 되는 최소 N을 구해보시오.
"""

from itertools import permutations

primes = [2, 3, 5, 6, 7, 11, 13]
m_value = primes[-1] * primes[-1]  # 최대로 가장 큰 것의 제곱
m_friend = []
for prime in permutations(primes):  # 6개의 요소
    friends = [prime[i] * prime[i + 1] for i in range(len(prime) - 1)]
    friends += [prime[0] ** 2, prime[-1] ** 2]

    if m_value > max(friends):  # 최소를 갱신한 경우
        m_value = max(friends)
        m_friend = friends

m_friend.sort()
print("정렬된 값:",m_friend)
print("합성 수:",m_value)

'''
배열의 인덱스에 -1을 지정하면 맨  마지막 요소를 얻을 수 있다.
'''
