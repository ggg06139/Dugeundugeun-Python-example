import random
x1 = random.randint(0,9)
x10 = random.randint(0,9)
y = int(input('복권 번호를 입력하세요 (0과 99사이)'))
print(f'당첨번호는 {x1}{x10}입니다.')
if y < 10:
    y1 = 0
    y10 = y
else:
    y10 = y//10
    y1 = y-y10*10

result = 0
if (x1==y1):
    result += 1
if (x1==y10):
    result += 1
if (x10==y1):
    result += 1
if (x10==y10):
    result += 1

if result >=2:
    print('상금은 100만원입니다.')
elif result ==1:
    print('상금은 50만원입니다.')
else:
    print('상금은 0원입니다.')
