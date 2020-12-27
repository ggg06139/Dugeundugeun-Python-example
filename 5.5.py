import random
x1 = random.randint(1,100)
x2 = random.randint(1,100)

ans = int(input(f'{x1}-{x2}='))

if ans == (x1-x2):
    print('맞았습니다')
else:
    print('틀렸습니다')
