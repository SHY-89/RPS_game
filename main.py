import random


def check_choice():
    u_c = input("가위,바위,보 중 하나를 선택해 주세요:")
    while u_c != '가위' and u_c != '바위' and u_c != '보':
        print("잘 못 입력 하였습니다. 다시 입력 하세요.")
        u_c = input("가위,바위,보 중 하나를 선택해 주세요:")
    return u_c


def game_start():
    game_status = True
    rps = {'가위': 1, '바위': 2, '보': 3}
    computer = ['가위', '바위', '보']
    game_save = {
        'win': 0,
        'lose': 0,
        'draw': 0,
    }
    while game_status:
        choice = random.choice(computer)
        user = check_choice()
        if user == choice:
            print("비겼 습니다.")
            game_save['draw'] += 1
        elif (choice == '가위' or choice == '보') and (user == '가위' or user == '보'):
            if rps[choice] % 3 > rps[user] % 3:
                print("컴퓨터 승리!!")
                game_save['lose'] += 1
            else:
                print("사용자 승리!!")
                game_save['win'] += 1
        else:
            if rps[choice] > rps[user]:
                print("컴퓨터 승리!!")
                game_save['lose'] += 1
            else:
                print("사용자 승리!!")
                game_save['win'] += 1

        y_n = input("다시 하시겠습니까? (y/n):")
        while y_n != 'y' and y_n != 'n':
            print("잘 못 입력 하였습니다. 다시 입력 하세요.")
            y_n = input("다시 하시겠습니까? (y/n):")
        if y_n == 'n':
            game_status = False

    vag = (game_save['win']) / (game_save['win'] + game_save['lose']) * 100
    print(f"승 : {game_save['win']}   패 : {game_save['lose']}   무 : {game_save['draw']}   승률 : {vag}%")


print("가위 바위 보 게임 START")
print("가위 바위 보 게임 Rule")
print("1. 사용자는 가위, 바위, 보, 만 입력 가능 합니다.")
print("2. 사용자는 게임이 끝난 뒤 y, n 만 입력 가능 합니다.")

print("게임 Rule을 이해 하셨다면 이제 게임을 즐겨주세요!!!")
game_start()
