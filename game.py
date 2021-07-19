import random

sel = ['가위', '바위', '보']
result = {0: '승리했습니다.', 1: '패배했습니다.', 2: '비겼습니다.'}


def checkWin(you, com):

    if not you in sel:
        print('잘못입력하였습니다. 다시 입력하세요')  # 가위,바위,보 가 아닌 다른 문자를 적었을 때.
        return False

    print(f'당신 ( {you} vs {com} ) 컴퓨터')  # 0 : win , 1 : lose , 2 : drew
    if you == com:
        state = 2  # 비겼을 때
    elif you == '가위' and com == '바위':  # 사람: 가위 였을 때 컴퓨터: 바위 였을 경우에는 컴이 이김
        state = 1
    elif you == '바위' and com == '보':
        state = 1
    elif you == '보' and com == '가위':
        state = 1
    else:
        state = 0
    print(result[state])
    return True


print('\n-------------------------------------------')
while True:  # 반복
    you = input("가위,바위,보 하나를 선택하세요.  >>>>   ")
    com = sel[random.randint(0, 2)]
    if checkWin(you, com):
        break
print('-------------------------------------------\n')
