import random

random_number = random.randint(1, 100)

#print(random_number)

game_count = 1

while True:

    try:
        my_number = int(input("1-100 사이 숫자를 입력하세요  : "))
    
    except:
        print('다시 입력하세요.')
        my_number = int(input("1-100 사이 숫자를 입력하세요  : "))

        if my_number > random_number:
            print('Down!!')

        elif my_number < random_number:
            print('Up!!')

        else:
            print(f'축하합니다. {game_count}번만에 맞추셨습니다.')
            break

        game_count += 1


# ctrl K & C 주석 추가
# ctrl K & U 주석 제거