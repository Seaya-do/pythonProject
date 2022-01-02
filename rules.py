# 수열의 사칙연산
# 1,000 ~ 9,999중에서 완성된 식의 계산 결과가 원래 수를 거꾸로 나열한 숫자로 되는 것을 구하시오.
import re

op = ["*", ""]
for i in range(1000, 10000):
    c = str(i)
    for j in range(0, len(op)):
        for k in range(0, len(op)):
            for l in range(0, len(op)):
                vs = c[3] + op[j] + c[2] + op[k] + c[1] + op[l] + c[0]

                # 0으로 시작하는 숫자가 있는지 확인하고 있는경우 제거
                vs = re.sub(r"0(\d+)", r"\1", vs)

                # 연산자를 하나는 넣는 경우
                if len(vs) > 4:
                    if i == eval(vs):
                        print(vs, "=", i)
