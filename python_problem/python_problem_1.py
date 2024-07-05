import random
num=0
number=1
player = 'A'

while number <=31:

    num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

    try: 
        num=int(num)
        if num not in [1, 2, 3]:
            print("1, 2, 3 중 하나를 입력하세요")
            continue

    except ValueError:
        print("정수를 입력하세요")
        continue


    for i in range(num):
        print(f"player {player} : {number}")
        number += 1

        if number > 31:
            break

        
        if player == 'A':
            player = 'B'
        else:
            player= 'A'


    #while True:
        #num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

        #try: 
            #num=int(num)
            #if num not in [1, 2, 3]:
                    #print("1, 2, 3 중 하나를 입력하세요")
                    #continue

        #except ValueError:
            #print("정수를 입력하세요")
            #continue




