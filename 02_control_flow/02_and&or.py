age = int(input("How old are you?")) #오직 하나의 argument만 받고, console입력 값이 input()의 return value이다. 값비교를 위해 int()함수를 사용해 숫자형타입으로 바꿔준다.
print("user answer", age)

print(type(age)) #변수의 type을 알려주는 built-in함수이다. 키보드로 입력했기 때문에 str(string)타입이다.

if age < 18:
    print("You can't drink.")
elif age >= 18 and age <= 35: #and는 두 조건 다 true여야 한다.
    print("You drink beer!")
elif age == 60 or age ==70: #or은 두 조건 중 하나만 true면 true이다.
    print("Birthday party!")
else:
    print("Go ahead!")

True and True == True
False and True == False
True and False == False
False and False == False

True or True == True
False or True == True
True or False == True
False or False == False