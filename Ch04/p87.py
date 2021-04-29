"""
chapter04.lecture.step02_list.py
"""

# (1) 단일 리스트 객체 생성
a = ['a', 'b', 'c']
print(a)

# (2) 중첩 리스트 객체 생성
b = [10, 20, a, 5, True, '문자열']  # 서로 다른 자료형
print(b[0])  # 10
print(b[2])  # 중첩 list
print(b[2][0])
print(b[2][1:]) # 중첩 list 2번 이후 원소