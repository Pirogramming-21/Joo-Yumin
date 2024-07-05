import random
num=0

num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

try: 
    int_num = int(num)
except ValueError:
    print("정수를 입력하세요")
    num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")


try:
    num = int(num)
    if num < 1 or num >3:
        print("1,2,3 중 하나를 입력하세요")
        num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
except ValueError:
    pass

playerA_number = 1
if num > 0:
    for i in range(num):
        print(f"playerA : {playerA_number}")
        playerA_number += 1


while True:
    num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

    try: 
        num=int(num)
        if num not in [1, 2, 3]:
                print("1, 2, 3 중 하나를 입력하세요")

        else:
            break
    except ValueError:
        print("정수를 입력하세요")



playerB_number = playerA_number
for i in range(num):
    print(f"playerB : {playerB_number}")
    playerB_number += 1
