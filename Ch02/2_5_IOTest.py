# Input Output test (입출력 테스트 )
"""
날짜 : 2021/04/27
이름 : 이지영
내용 : 파이썬 표준입출력 실습 _ 교재 p42
"""

# 파이썬 표준 출력
print('hello', end='!') #print : 출력함수 (자바에선 document.write('hello');)
print('python')

print('010', '1234', '1111', sep='-') # seperate 값

# 파이썬 표준 입력
num = input('숫자입력 : ')

print('입력한 숫자 :', num)
print('num type :', type(num))

# 입력받은 문자열을 숫자로 변환하는 작업이 필요함. <class 'str'> 문자열로 읽히기 때문
result = int(num)
print('result :', result)
print('result type :', type(result))


# 서식문자 출력
print('%d년 %d월 %d일 %s요일' % (2021, 4, 27, '화')) # %s: string 문자열을 나타냄

# 포맷문자 출력
print('이름 : {}, 나이 : {}, 주소 : {}' .format('김유신', 23, '김해시'))

