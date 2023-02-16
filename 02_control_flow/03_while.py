"""#모듈에서 default로 포함 된(built-in) function들 == the python standard library, import만 하면 된다.
# import random
from random import randint

user_choice = int(input("Choose number."))
pc_choice = randint(1, 50)

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower! Computer Choose", pc_choice)
elif user_choice < pc_choice:
    print("Higher! Computer Choose", pc_choice)
"""

#================================================
"""
distance = 0
while distance <= 20: #if문처럼 조건문이 true라면 while문 안의 코드는 계속 실행된다. 비로소 false가 된다면 멈춘다.
    print("I'm running:",distance,"km")
    distance = distance + 1
"""
#================================================
from random import randint

print("==========python casino==========")
pc_choice = randint(1, 50)

playing = True

while playing: #True일때만 반복한다.
    user_choice = int(input("Choose number(1~50):"))
    if user_choice == pc_choice:
        print("You won!")
        playing = False #더이상 반복되지 않는다.
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher!")