#========Method : 데이터 뒤에 결합/연결된 function.=========
name = "seo" #String 내부에는 많은 Method을 내포하고 있다.
print(name.upper()) #텍스트를 대문자로 만들어 준다.
print(name.capitalize()) #텍스트의 첫글자만 대문자로 만들어 준다.
print(name.startswith("s")) #첫글자를 체크해서 boolean으로 반환 해준다.
print(name.replace("o","❤")) #해당 글자를 찾아서 원하는 글자로 대체 해준다.
#이처럼 데이터를 가지고 method를 통해 데이터를 변환하고 조작할 수 있다.

print("==============list==============")
#쉼표를 사용해서 데이터를 분리한다.

days_of_week = ["Mon","Tue","Wed","Thur","Fri"]
print(days_of_week)
print(days_of_week[2])
print(days_of_week.count("Wed")) #list안에 해당 문자와 같은 문자를 찾아 갯수를 리턴해준다.
days_of_week.append("Sat")
print("append1 :",days_of_week)
days_of_week.append("Sun")
print("append2 :",days_of_week)
days_of_week.remove("Mon")
print("remove :",days_of_week)
days_of_week.reverse()
print("reverse :",days_of_week)
days_of_week.clear() #data를 modify(수정) or mutate(변화), 리스트들의 아이템을 삭제!
print("clear :",days_of_week)