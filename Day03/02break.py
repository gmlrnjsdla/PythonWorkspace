list = [1, 2, 3, 5, 7, 2, 5, 237, 55]
for val in list:
    if val % 3 == 0:  # val을 3으로 나눈 나머지가 0이면
        print(val)    # val을 출력한다.
        break
        