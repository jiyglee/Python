# 클래스 정의
class Account:   # class 는 대문자로 정의함
    # 계좌속성
    def __init__(self, bank, id, name, money):  # __init__ 특수함수
        self.bank = bank
        self.id = id
        self.name = name
        self.money = money

     # 계좌기능 (입금, 출금, 잔액조회)
    def deposit(self, money):
        self.money += money

    def withdraw(self, money):
        self.money -= money

    def show(self):
        print('-------------------')
        print('은행명 : ', self.bank)
        print('계좌번호 : ', self.id)
        print('입금주 : ', self.name)
        print('현재잔액 : ', self.money)
