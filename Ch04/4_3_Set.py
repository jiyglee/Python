"""
날짜 : 2021/04/27
이름 : 이지영
내용 : 파이썬 자료구조 Set 실습 _ 교재 p96
"""

# set은 순서 상관없고, 중복안됨. (list는 순서있고, 중복가능)

# Set 생성
set1 = {1, 2, 3, 4, 5, 3} # list= [] , tuple = ()
print('set1 type :', type(set1))
print('set1 :', set1)  # 마지막3은 중복이라서 결과값에 안보인다.

set2 = set('Hello World')
print('set2 type :', type(set2))
print('set2 :', set2)

# set 출력 -> list화 해서(list로 변환) 하나씩 출력한다
list1 = list(set1) #순서는 랜덤임. 알수없다. 하지만 기본적으로 1,2,3,4로 될거
print('list1 :', list1)
print('list1[0] :', list1[0])
print('list1[3] :', list1[3])

list2= list(set2) # 순서는 출력할때마다 달라짐
print('list2 :', list2)
print('list2[0] :', list2[0])
print('list2[3] :', list2[3])
