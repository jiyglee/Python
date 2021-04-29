"""
날짜 : 2021/04/29
이름 : 이지영
내용 : 파이썬 리스트 함수 _ 교재 p88
"""

dataset = [1, 4, 3]
print('1.dataset :', dataset)


# List 원소 추가
dataset.append(2)  # 자주사용하는 append : 뒤에 추가하라는 뜻
dataset.append(5)
print('2.dataset :', dataset)

# List 정렬
dataset.sort()
print('3.dataset :', dataset)  # 오름차순

dataset.sort(reverse=True)
print('4.dataset :', dataset)  # 내림차순

# List 원소 삽입
dataset.insert(2, 6)
dataset.insert(1, 7)
print('5.dataset :', dataset)
# index 번호 [0, 1, 2, 3, 4, 5] 이렇게 있는데,
# 5.dataset은 index 2번에 6을 삽입하라는 뜻

# List 원소 삭제
dataset.remove(6)
print('6.dataset:', dataset) # 6을 삭제하라

# map 함수
# - 리스트 원소를 지정된 함수로 일괄 처리해주는 함수
# - 여러개의 데이터를 한번에 다른 형태로 변환할 때 많이 사용
def plus10(n):
    return n+10

list1 = [1, 2, 3, 4, 5]
list1_map_list = list(map(plus10, list1))
print('list1_map_list :', list1_map_list)

list2 = [1.1, 2.2, 3.3, 4.4, 5.5]
list2_map_list = list(map(int,list2))
print('list2_map_list :', list2_map_list)

var1 = 2135.2684321
result = int(var1)  # 실수 -> 정수 변경
print('result :', result)

list3 = [1, 2, 3, 4, 5]
list3_map_list = list(map(lambda x:x*2, list3))
print('list3_map_list :', list3_map_list)

list4 = ['1', '2', '3', '4', '5']
list4_map_list = list(map(int,list4))
print('list4_map_list :', list4_map_list)

var2 = '1'
result = int(var2)  # 문자 -> 숫자 변환(*이게 제일 많이 사용)
print('result :', result)

# input 함수 확장 (파이썬 기본 입력함수)
a = input('입력 :')
print('a :', a)

var1, var2, var3 = input('3개 숫자 입력(띄어쓰기 구분) : ').split()
print('var1 : {}, var2 : {}, var3 : {}'.format(var1, var2, var3))
print('var1 + var2 + var3 = ', var1+var2+var3) # 문자열덧셈

num1, num2, num3 = map(int, input('3개 숫자 입력(띄어쓰기 구분 : ').split())
print('num1 : {}, num2 : {}, num3 : {}'.format(num1, num2, num3))
print('num1 + num2 + num3 = ', num1+num2+num3) # 숫자 덧셈

