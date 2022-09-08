# # list index out of range 에러발생
# list1 = []  # 비어있는 리스트 생성
# print(list1[0])
#==============================================================

# # 형변환 에러
# text1 = 'abc'
# print(int(text1))

# text1 = 'abc'
#
# try:
#     print(int(text1))
# except ValueError:
#     print('문자는 숫자로 바꿀 수 없습니다. 다시 확인해주세요')
#=============================================================

# def safe_pop_print(list, index):
#     try:
#         print(list.pop(index))   # index에 해당하는 값을 지우면서 출력합니다.
#     except IndexError:
#         print('{} index의 값을 가져올 수 없습니다.'.format(index))
#
#
# list1 = [1, 2, 3, 4, 5]
# safe_pop_print(list1, 5)
# print(list1)
#===========================================================

def divide(a, b):
    try:
        mok = a / b
        print(mok)
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')

# divide(20, 0)

#==========================================================

def divide2(a, b):
    if b==0:
        print('0으로 나눌 수 없습니다.')
    else:
        mok = a / b
        print(mok)

num2 = input('100을 나눌 피젯수를 입력하세요 >> ')
num2 = int(num2)

while num2 == 0:
    print('피젯수는 0이 될 수 없습니다!')
    num2 = input('100을 나눌 피젯수를 입력하세요 >> ')
    num2 = int(num2)

divide(20,num2)
divide2(20, num2)

