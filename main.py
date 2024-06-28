import random

rps = {'가위': 1, '바위': 2, '보': 3}

computer = ['가위', '바위', '보']
choice = random.choice(computer)

user = input("가위,바위,보 중 하나를 선택해 주세요:")
if user == choice:
    print("비겼 습니다.")
elif (choice == '가위' or choice == '보') and (user == '가위' or user == '보'):
    if rps[choice] % 3 > rps[user] % 3:
        print("졌 습니다")
    else:
        print("이겼 습니다.")
else:
    if rps[choice] > rps[user]:
        print("졌 습니다")
    else:
        print("이겼 습니다.")
