# 튜플 설명
# tuple은 한번 만들면 변경 X
# tuple1 = (1, 2, 3, 4, 5)  # 튜플 선언
#
# tuple2 = 1, 2, 3, 4, 5  # 튜플 선언2

# print(type(tuple1))
# print(tuple2[2])
#
# for tuple in tuple1:
#     print(tuple)
#
# for i in range(len(tuple1)):
#     print(tuple1[i])

# list = [1, 2, 3, 4, 5]
# list[1] = 100
# del list[1]
# print(list)

# # tuple1[1] = 100  # 값 변경 X
# # del tuple1[1]  # 값 삭제 X  // pop, append, remove 등 수정안됨
# print(tuple1)

#================================================================

# 패킹, 언패킹, 특징
a, b = 1, 2
print(a)
print(b)
print(type(a))
c = (3, 4)  #튜플 c 선언
print(type(c))
print('===========================================')

d, e = c  # 언패킹
print(d)
print(e)
print(type(d))
print('===========================================')

f = 10
g = 20
h = f, g
print(h)
print(type(h))  # 패킹
print('===========================================')

def sum_and_mul(a, b):
    sum = a + b
    mul = a * b
    return sum, mul   # 동시에 return 시 튜플로 반환

result = sum_and_mul(10, 20)
print(result)
print(type(result))
print('a + b =', result[0])
print('a * b =', result[1])
