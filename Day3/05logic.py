import random

# kor = None
# eng = None
# math = None
# sci = None
#
# kor = int(input('국어점수 입력 >>'))
# eng= int(input('영어점수 입력 >>'))
# math = int(input('수학점수 입력 >>'))
# sci = int(input('과학점수 입력 >>'))
#
# # 4과목 모두 90점 이상일 때 장학금 대상
# if kor >= 90 and eng >= 90 and math >= 90 and sci >= 90:
#     print('장학금 대상 and')
#
# # 4과목 중 1과목만 90점 이상이면 장학금 대상
# if kor >= 90 or eng >= 90 or math >= 90 or sci >= 90:
#     print('장학금 대상 or')

#============================================================

# a = 10
# b = 20
# list = []
# print(bool(list))  # 0,None 을 제외한 모든 수는 TRUE
#
# if a:
#     mok = a / b
#     print('a/b = ', mok)
#     print('a는 null이 아닙니다!')
# else:
#     print('a는 null 입니다!')
#=============================================================

# 로또 번호 생성기

# def lotto_output():
#     lottoNumber = random.randint(1, 45)  # 1~45 수중 1개의 랜덤 정수 추출
#     return lottoNumber
#
# def lotto_game():
#     list = []
#     while True:
#         lottoNum = lotto_output()
#         # if lottoNum in list:  #새로 추출한 랜덤숫자가 기존 리스트에 없을 경우에만 추가
#         #     continue
#         if lottoNum not in list:
#             list.append(lottoNum)
#         if len(list) == 6:
#             break
#     list.sort()
#     print(list)
#
#
# num = input('게임 횟수 >> ')
# num = int(num)
#
# for i in range(num):
#     print('게임{}'.format(i+1), end=' ')
#     lotto_game()

#===================================================================

# 가위바위보

# win = 0
# lose = 0
# draw = 0
# user = input('가위, 바위, 보 중 1개를 입력하세요 (0 -> 게임종료)>> ')
# com = random.choice(['가위', '바위', '보'])
# while True:
#
#     if user == '0':                  # 0 입력했을때
#         print('게임을 종료합니다.')     # 출력
#         break                        #break
#     elif user == com:
#         print('당신은 [{}], 컴퓨터는 [{}]를 냈습니다.'.format(user, com))
#         print('무승부 입니다.')
#         draw = draw + 1
#     elif (user == '가위' and com == '보') or \
#             (user == '바위' and com == '가위') or \
#             (user == '보' and com == '바위'):
#         print('당신은 [{}], 컴퓨터는 [{}]를 냈습니다.'.format(user, com))
#         print('당신이 승리하였습니다.')
#         win = win + 1
#     else:
#         print('당신은 [{}], 컴퓨터는 [{}]를 냈습니다.'.format(user, com))
#         print('컴퓨터가 승리하였습니다.')
#         lose = lose + 1
#     user = input('가위, 바위, 보 중 1개를 입력하세요 (0 -> 게임종료)>> ')
#     com = random.choice(['가위', '바위', '보'])
#
# print('게임결과 : {}전 {}승 {}패 {}무'.format(win+lose+draw, win, lose, draw))

#과제 
# 사용자로부터 수를 입력받아 컴퓨터가 생각한 수를 맞추는 게임

# [출력화면]
# 남은 출력 횟수 : 20
# 컴퓨터가 생각한 수를 맞춰보세요(1~99) >> 55
# 틀렸습니다. 컴퓨터의 수는 55보다 큰 수입니다.
# 남은 출력 횟수 : 19
# 컴퓨터가 생각한 수를 맞춰보세요(1~99) >> 60
# 정답입니다. 게임을 종료합니다.

# 몇번만에 맞췄는지 출력
# 남은 시도 횟수 : 20 19 18 ...0 이면 게임종료
