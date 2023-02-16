if 10 > 5:
    print("True1") #whitespace(공백)가 필요하다.

if 10 >= 5:
    print("True2")

if 2 <= 5:
    print("True3")

if 5 == 5:
    print("True4")

a = 10
if a == 10:
    print(True)

b = "seo"
if b =="seo":
    print(True)

print("=====================================")

#password_correct = True
password_correct = False
if password_correct:
    print("Here is your money")
else: #선택사항
    print("Wrong password")

print("=====================================")

#winner = 9
#winner = 11
winner = 10
if winner > 10:#조건에 부합한다면 아래의 코드들을 실행조차 하지 않는다.
    print("Winner is greater than 10")
elif winner < 10: #코드에 또 다른 조건과 대안을 넣을 수 있도록 해준다.
    print("Winner is less than 10")
else: #조건이 true가 아닐 때의 대안만 제공해준다.
    print("Winner is 10")
