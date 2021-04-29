"""
chapter04.lecture.step02_list.py
"""

# (1) 리스트 결합
x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y   # new object
print(z)

# (2) 리스트 확장
x.extend(y)  # x확장
print(x)

# (3) 리스트 추가
x.append(y)  # x추가
print(x)

# (4) 리스트 두배확장
lst = [1, 2, 3, 4]  # list 생성
result = lst * 2  # 각 원소 연산은 안됨
print(result)

"""
p90
"""
# (1) 리스트 정렬
print(result)
result.sort()  # 오름차순 정렬
print(result)
result.sort(reverse = True)  # 내림차순 정렬
print(result)

# (2) 리스트 요소 검사
import random
r = []  # 빈 list
for i in range(5):
    r.append(random.randint(1,5))

print(r)
if 4 in r :
    print('있음')
else :
    print('없음')