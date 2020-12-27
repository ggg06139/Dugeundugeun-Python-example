phone_book = {}
while True:
    a = input('(입력모드) 이름을 입력하시오:')
    if a != '':
        b = input('전화번호를 입력하시오:')
        phone_book[a] = b
    else:
        while True:
            c = input('(검색모드) 이름을 입력하시오:')
            print(f'{c}의 전화번호는 {phone_book[c]}입니다.')