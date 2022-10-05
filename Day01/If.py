a = 100
b = 100
c = 200

# if a < b:  #if문 다음 줄에는 반드시 들여쓰기를 해야한다.
#     print("a는 b보다 작다.")
# else:
#     print('a는 b보다 크다.')
# print('안녕하세요!!!')

# if a != c :  #같지 않다.
#     print('a와 c는 같지 않습니다.')

if a == b and a != c:  #TRUE and TRUE
    print('a와 b는 같고, a와 c는 같지 않습니다.')

if a == b and a > c:  #TRUE and FALSE
    print('a와 b는 같고, a는 c보다 크다.')

if a == b or a > c:  #TRUE or FALSE
    print('a와 b는 같고, a는 c보다 크다.')


