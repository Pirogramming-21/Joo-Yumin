import random

def brGame(player):
    number = 1
    while number <= 31:
        num = input(f"player{player}, 부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        
        try: 
            num = int(num)
            if num not in [1, 2, 3]:
                print("1, 2, 3 중 하나를 입력하세요")
                continue

        except ValueError:
            print("정수를 입력하세요")
            continue

        for i in range(num):
            print(f"player{player} : {number}")
            number += 1

            if number > 31:
                return player
        
        if player == 'A':
            player = 'B'
        else:
            player = 'A'

    return player

player = 'A'
brGame(player)
winner = 'B' if player=='A' else 'A'
print(f"player{winner} win!")




