"""
chapter04.lecture.step02_list.py
"""

# (1) 단일 list 예
lst = [1, 2, 3, 4, 5]
print(lst)
print( type(lst))

for i in lst :
    print(lst[:i])  # i전까지
