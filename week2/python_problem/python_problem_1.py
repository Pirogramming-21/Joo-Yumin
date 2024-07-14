import random

def brGame(player):
    number = 1
    while number <= 31:
        if player=='player':
            num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        
            try: 
                num = int(num)
                if num not in [1, 2, 3]:
                    print("1, 2, 3 중 하나를 입력하세요")
                    continue

            except ValueError:
                print("정수를 입력하세요")
                continue


        else:
            num = random.choice([1, 2, 3])

        for i in range(num):
            print(f"{player} : {number}")
            number += 1

            if number > 31:
                return player
        
        if player == 'player':
            player = 'computer'
        else:
            player = 'player'

    return player

player = 'player'
brGame(player)
winner = 'computer' if player=='player' else 'player'
print(f"player{winner} win!")




