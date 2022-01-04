# 콜라츠 추측(Collatz Conjecture)
# 자연수 n이 짝수인 경우, n을 2로 나눈다.
# n이 홀수인 경우, n에 3을 곱해 1을 더함
# 이 계산을 반복하면 초깃값이 어떤 수였더라도 반드시 1에 도달함, 6은 예외
# 처음 값은 3을 곱하고 1을 더함
def loop(n):
    check = n * 3 + 1
    while check != 1:
        check = check // 2 if check % 2 == 0 else check * 3 + 1
        if check == n:
            return True
    return False


# 10,000 이하의 짝수 중 앞의 2나 4와 같이 처음의 수로 돌아가는 수가 몇개인가
cnt = 0
for i in range(2, 10000 + 1, 2):
    if loop(i):
        cnt += 1
print("답은 :",cnt)
