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

try: 
    num = int(num)
    for i in range(1, num+1):
        print(f"playerA: {i}")
except ValueError:
    pass