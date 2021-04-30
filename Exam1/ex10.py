"""
날짜 : 2021/04/30
이름 : 이지영
내용 : 파이썬 이진검색 연습문제
"""

dataset = [5, 10, 18, 22, 35, 55, 75, 103, 152]
value = int(input('검색할 숫자 입력 : '))

start = 0
end = len(dataset) - 1
loc = 0
state = False

while start <= end:
    mid = (start + end) // 2   # 4

    if dataset[mid] > value:
        end = mid - 1          # 3
    elif dataset[mid] < value:
        start = mid + 1        # 5
    else:
        loc = mid
        state = True         # 상태 변수
        break

if state:
    print('찾은 위치 : %d번째' % (loc + 1))
else:
    print('찾는 숫자가 없습니다.')
