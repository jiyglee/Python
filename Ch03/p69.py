"""
날짜 : 2021/04/28
chapter03.lecture.step02_while.py
"""

i = 0
while i < 10 :
    i += 1   # 카운터
    if i == 3 :
        continue   # 다음문장 skip
    if i == 6 :   # 탈출조건
        break    #exit
    print(i, end=' ')

