list1 = [1,2,3,4,5]
a = 10

for i in list1:
    print(i)

# 자바 for문(list1의 모든 원소 출력)
# for(int i=0;i<5;i++) {
#     print(list1[i])
# }

# 자바 for문(1부터 10까지 출력)
# for(int i=0;i<10;i++) {
#     System.out.println(i+1);
# }
print('----------------------------')
list2 = ['호랑이','고양이','강아지','사자','원숭이']
for i in range(4): # 0 1 2 3
    print(list2[i])

print('----------------------------')
for i in list2:
    print(i)

print('----------------------------')
for i in range(len(list2)): # 리스트의 길이를 자동으로 측정
    # len() : 리스트의 원소의 개수를 반환하는 함수
    print(list2[i])

print('----------------------------')

for i, animal in enumerate(list2):
    print('list2 리스트의 {}번째 원소는 {}입니다.'.format(i+1,animal))





