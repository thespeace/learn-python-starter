#define : 정의하다 / function : 기능 / 작동(기능)하다

def say_hello(user_name): #parameter(매개변수)
    print("hello", user_name, "how are you?")
#위 코드처럼 두 칸 띄여줘야한다.
#파이썬은 빈 공백은 코드에 영향을 크게 미친다. 중괄호대신 공백을 사용한다.

say_hello("a") #argument(인자)
say_hello("b")
say_hello("c") #코드 재사용!

def say_bye(user_name, user_age):
    print("hello", user_name)
    print("you are", user_age, "years old")

say_bye("seo", 12)

def say_hello(user_name="anonymous"): #만약 매개변수를 정의하지 않았다면 anonymous를 출력한다.
    print("hello", user_name)

say_hello()



###############Practice : Make Calculator, Make Juice
#오류값은 0이여야 한다.

def plus(a=0,b=0):
    print(a + b)
plus()

def minus(a=0,b=0):
    print(a - b)
plus()

def multiplication(a=0,b=0):
    print(a * b)
multiplication()

def division(a=0,b=1):
    print(a / b)
division()

def Square(a=0,b=1):
    print(a ** b)
Square()

print("---------------------------")

def tax_cal(money):
    return money * 0.35

def pay_tax(tax):
    print("thanks you for paying", tax)

pay_tax(tax_cal(15000))

print("---------------------------")

my_name = "seo"
my_age = 31
my_color_eyes = "brown"

#f"" : format이라는 뜻의 f를 넣어주면 문자열을 변수로 만들 수 있다.
print(f"Hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color")

print("---------------------------")

def make_juice(fruit):
    return f"{fruit}+🥤"
    print("nononononononono")

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🍬"

juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)