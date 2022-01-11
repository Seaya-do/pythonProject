"""
연월일을 YYYYMMDD의 8자리 정수로 나타냈을 때 2진수로 변환하여 거꾸로 나열한
다음 다시 10진수로 되돌렸을 때 원래 날짜와 같은 날짜가 되는것을 찾아라.
기간 1964년 10월10일 ~ 2020년 7월 24일
"""

from datetime import datetime, timedelta

from_left = int(bin(19641010).replace("0b", "")[4:4 + 8], 2)
to_left = int(bin(20200724).replace("0b","")[4:4 + 8], 2)

for i in range(from_left, to_left + 1):
    l = "{0:08b}".format(i)
    r = l[::-1]
    
    for m in range(0, 1 + 1):
        value =  "1001{}{}{}1001".format(l,m,r)
        try:
            date = datetime.strptime(str(int(value, 2)),"%Y%m%d")
            print(date.strftime("%Y%m%d"),"일")
            
        except:
            pass