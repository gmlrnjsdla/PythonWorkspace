#과제
# 사용자로부터 수를 입력받아 컴퓨터가 생각한 수를 맞추는 게임

# [출력화면]
# 남은 시도 횟수 : 20
# 컴퓨터가 생각한 수를 맞춰보세요(1~99) >> 55
# 틀렸습니다. 컴퓨터의 수는 55보다 큰 수입니다.
# 남은 출력 횟수 : 19
# 컴퓨터가 생각한 수를 맞춰보세요(1~99) >> 60
# 정답입니다. 게임을 종료합니다.
# 몇번만에 맞췄는지 출력
# 남은 시도 횟수 : 20 19 18 ...0 이면 게임종료
#========================================================================
import random

life = 20
count = 0
print('남은 시도 횟수 : ', life)
com = random.randint(1, 99)
print(com)

while True:
    user = int(input('컴퓨터가 생각한 수를 맞춰보세요(1~99) >> '))
    if user == com:
        print("정답입니다. 게임을 종료합니다.")
        print('시도 횟수 : ', count)
        break
    elif life == 1:
        print('시도 횟수를 모두 사용하셨습니다. 정답은 {}였습니다. 게임을 종료합니다.'.format(com))
        break
    elif user > com:
        print("틀렸습니다. 컴퓨터의 수는 {}보다 작은 수입니다.\n".format(user))
        life = life - 1
        count = count + 1
    else:
        print("틀렸습니다. 컴퓨터의 수는 {}보다 큰 수입니다.\n".format(user))
        life = life - 1
        count = count + 1
    print('남은 시도 횟수 : ', life)

