"""
날짜 : 2021/04/29
이름 : 이지영
내용 : 파이썬 클래스 실습하기 _ 교재 p148
"""

from Ch06.sub1.Account import Account
from Ch06.sub1.Computer import Computer


# account 객체 생성

kb = Account('국민은행', '101-12-1010', '김유신', 10000)
# class의 함수 __init__를 실행해라(인자값4개)
kb.deposit(40000)
kb.withdraw(7000)
kb.show()

wr = Account('우리은행', '101-12-1911', '김춘추', 100000)
wr.deposit(10000)
wr.withdraw(5000)
wr.show()

# Computer 객체 생성
samsung = Computer('Samsung', 'Intel i7', '16GB', '1TB')
imac = Computer('Apple', 'Intel i7', '32GB', '1TB')

samsung.info()
imac.info()



