
# 1부터 10까지 짝수 합
sum2 = 0

for k in range(11):

    if k % 2 == 0:
        sum2 = k

print('1부터 10까지 짝수 합:', sum2)

# 중첩 for
for a in range(3):
    print('a :', a)

    for b in range(4):
        print('b :', b)

# 구구단
for x in range(2, 10):
        print(x, '단')

    for y in range(1, 10):
        z = x * y
        print('%d x %d = %d' % (x, y, z))


