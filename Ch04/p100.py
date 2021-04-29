"""
chapter04.lecture.step05_dict.py
"""

# (1) dict 생성 방법 1
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic)

# (2) dict 생성 방법2
person = {'name' : '홍길동', 'age': 35, 'address' : '서울시'}
print(person)
print(person['name'])
print(type(dic), type(person))

# (3) 원소 수정, 삭제, 추가
# dict 원소 수정
person['age'] =45
print(person)

# dict 원소 삭제
del person['address']
print(person)

# dict 원소 추가
person['pay'] = 350
print(person)

# (1) 요소 검사
print(person['age'])
print('age' in person)

# (2) 요소 반복
for key in person.keys() : # key 넘김
    print(key)
for v in person.values() :  # value 넘김
    print(v)

for i in person.items() :  # (key, value) 넘김
    print(i)