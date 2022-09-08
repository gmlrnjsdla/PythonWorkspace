# selected = None  # =null
# while selected not in ['가위', '바위', '보']:
#     selected = input('가위, 바위, 보 중에 선택하세요 >> ')
#
# print('선택된 값은:', selected)


print('=================')
print('(1) 성적보기')
print('(2) 수강확인')
print('(3) 프로그램 종료')
print('=================')
menuNumber = input('메뉴 중 원하시는 번호를 선택해주세요 >> ')

while menuNumber not in ['1', '2', '3']:
    print('잘못된 베뉴 번호입니다. 다시 입력해주세요.')
    print('=================')
    print('(1) 성적보기')
    print('(2) 수강확인')
    print('(3) 프로그램 종료')
    print('=================')
    menuNumber = input('메뉴 중 원하시는 번호를 선택해주세요 >> ')

    print('선택하신 메뉴번호는 {}입니다.'.format(menuNumber))
