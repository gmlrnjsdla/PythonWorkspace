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

a = 10
b = 20
list = []
print(bool(list))  # 0,None 을 제외한 모든 수는 TRUE

if a:
    mok = a / b
    print('a/b = ', mok)
    print('a는 null이 아닙니다!')
else:
    print('a는 null 입니다!')
