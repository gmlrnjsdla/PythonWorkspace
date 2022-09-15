# 문제1) 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하시오.
#
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# <출력결과>
# 이름
# 나이
# 성별
dict1 = {"이름":"김말똥", "나이":30, "성별":0}


def print_keys(dict):
    for key in dict.keys():
        print(key)


print_keys(dict1)
print('=================================================')

# 문제2) 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하시오.

# make_list("abcd")

# ['a', 'b', 'c', 'd']


def make_list(name):
    name1 = [name[i] for i in range(len(name))]
    # name1 = []
    # for i in range(len(name)):
    #     name1.append(name[i])
    return name1


print(make_list("abcd"))
print('=================================================')

# 문제3) 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하시오.

# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]

su1 = [3, 4, 5, 6, 7, 8]


def pickup_even(list):
    list1 = [list[i] for i in range(len(list)) if list[i] % 2 == 0]
    # list1 = []
    # for i in range(len(list)):
    #     if list[i] % 2 == 0:
    #         list1.append(list[i])
    return list1


print(pickup_even(su1))
