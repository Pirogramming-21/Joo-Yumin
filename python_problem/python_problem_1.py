num=0

number = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")

try: 
    int_number = int(number)
except ValueError:
    print("정수를 입력하세요")
    number = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")


try:
    number = int(number)
    if number < 1 or number >3:
        print("1,2,3 중 하나를 입력하세요")
        number = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
except ValueError:
    pass