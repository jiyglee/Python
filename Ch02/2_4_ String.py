"""
날짜 : 2021/04/26
이름 : 이지영
내용 : 파이썬 String 예제_교재 p48
"""

# 문자열 더하기
str1 = 'Hello'
str2 = 'Python'
str3 = str1 + str2
print('str3 : ', str3)

# 문자열 곱하기
name = '홍길동'
print('name * 3 : ',name * 3)

# 문자열 길이 (문자의 개수(space bar 포함)
msg = 'Hello World'
print('msg 길이 : ', len(msg))


# 문자열 인덱스
# H/e/l/l/o/ /W/o/r/l/d
# 1/2/3/4/5/6/7/8/9/10/11
print('msg 1번째 문자 :', msg[0])
print('msg 7번째 문자 :', msg[7])
print('msg -1번째 문자 :', msg[-1]) # 뒤로 돌아감
print('msg -5번째 문자 :', msg[-5])

# 문자열 자르기(substring)
print('msg의 0~5까지 문자열 :', msg[0:5])
print('msg의 처음~5까지 문자열 :', msg[:5])
print('msg의 6~11까지 문자열 :', msg[6:11])
print('msg의 6~마지막까지 문자열 :', msg[6:])

# 문자열 분리
people = '김유신|김춘추|장보고|강감찬|이순신'
p1, p2, p3, p4, p5 = people.split('|')

print('p1 : ', p1)
print('p2 : ', p2)
print('p3 : ', p3)
print('p4 : ', p4)
print('p5 : ', p5)

# 문자열 이스케이프
print('서울\n대전\n대구\n부산\n광주') #한줄씩 띄워라
print('서울\t대전\t대구\t부산\t광주') #한tap씩 띄워라
print('저는 \'홍길동\'입니다.') #''를 문자로 출력한다는 뜻
print("저는 \'홍길동\'입니다.") # 파이썬은 ""로도 문자열 표시 가능(자바는 안됨)
