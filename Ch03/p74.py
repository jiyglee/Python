"""
날짜 : 2021/04/28
chapter03.lecture.step03_for.py
"""

# 구구단 출력 : range() 함수 이용

# (1) 바깥쪽 반복문
for i in range(2, 10):
    print('~~~ {}단 ~~~'.format(i))

    # (2) 안쪽 반복문
    for j in range(1,10):
        print('%d * %d = %d' % (i, j, i*j))