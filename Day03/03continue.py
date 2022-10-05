list = [1, 2, 3, 5, 7, 2, 5, 237, 55]
for i in range(len(list)):
    if list[i] % 2 != 0:  # i를 2로 나눈 나머지가 0이 아니면 홀수이므로
        print(list[i])    # 두 번 출력한다.


print('=================================================')

for i in range(len(list)):
    if list[i] % 2 == 0:  # i를 2로 나누어서 나머지가 0이면 짝수이므로
        continue    # 제외한다. 처음으로 돌아가기
    print(list[i])



sizes = [33, 35, 34, 37, 32, 35, 39, 32, 35, 29]
for i, size in enumerate(sizes):
    if size == 32:
        print("사이즈 32인 바지는 {}번째에 있다.".format(i+1))
        break

numbers = [(1, 2), (10, 0)]
for a, b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.")
        continue
    print('{}를 {}로 나누면 {}'.format(a, b, a/b))
