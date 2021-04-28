"""
날짜 : 2021/04/28
이름 : 이지영
내용 : 파이썬 반복문 While 실습_교재 p64

"""

# while

num1 = 1
while num1 < 5:
    print('num1 :', num1)
    num1 += 1

# 1부터 10까지의 합
k, sum = 1, 0

while k <= 10:
    sum += k
    k += 1

print('1부터 10까지의 합:', sum)


# continue
s, total = 1, 0

while s <= 10:

    s += 1
    if s % 2 == 1:
        # 반복문의 상위로 이동
        continue

       total = s
