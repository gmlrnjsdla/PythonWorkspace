# ** 파이썬 반복문 문제 **

# 문제1) 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하시오.
mul = 1

for i in range(1, 11):
    mul = mul * i

print(mul)
print('===========================================')
# 문제2) 리스트에 동물 이름 저장되어 있다.
# 리스트 = ['dog', 'cat', 'parrot']
# for문을 사용해서 동물 이름의 첫 글자만 출력하시오.

# <출력결과>
# d
# c
# p
animal_list = ['dog', 'cat', 'parrot']
for name in animal_list:
    print(name[0])
print('===========================================')

# 문제3) my_list를 아래와 같이 출력하시오.

# my_list = ["가", "나", "다", "라"]

# <출력결과>
# 가 나
# 나 다
# 다 라

my_list = ["가", "나", "다", "라"]

for i in range(len(my_list)-1):
    print(my_list[i], my_list[i+1])






