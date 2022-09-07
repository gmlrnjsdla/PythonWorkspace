# a = 100
# b = 90
# c = 60
# d = 70
# e = 50

# list0 = [1,2,3,4,5]
# list1 = [100, 90 ,60, 70, 50]
#
# list1.append(200)
#
# print(list1)
#
# list2 = list1 + [300]
# print(list2)
#
# listSum = list0 + list1
# print(listSum)
#
# ownership = 1000 in list1
# print(ownership)
#
# if 100 in list1:
#     print("100이 list1 안에 있습니다!")
#
# print('--------------------------------')
# list5 = [1,2,3,4,500]
# del list5[2]
# list5.remove(500)
# print(list5)
#
# # listSum = list1[3] + 100
# # print(listSum)
#
#
# list2 = ['호랑이', '고양이', '강아지', '사자', '원숭이']
#
# for i, animal in enumerate(list2):
#     print('list2 리스트의 {}번째 원소는 {}입니다. '.format(i+1, animal))

#=========================================================#
#1번
# for i in range(4):
#     print(i)

#=========================================================#
#2번
# rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
# for i in range(len(rainbow)):
#    color = rainbow[i]
#    print('{}번째 색은 {}'.format(i+1, color))

#=========================================================#
#3번
# rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
# for i, color in enumerate(rainbow):
#     print('{}번째 색은 {}'.format(i+1, color))

#========================================================#
#4번
days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i, day in enumerate(days):
    print('{}월의 날짜 수는 {}일 입니다.'.format(i+1, day))