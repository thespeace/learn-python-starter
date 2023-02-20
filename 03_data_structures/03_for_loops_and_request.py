#python standard library에 기본으로 포함되어 있지 않은 module을 다운로드 받았다.
from requests import get

websites = ( #이름을 복수형으로 지어주는 컨벤션이 있다.
    "google.com",
    "https://airbnb.com",
    "twitter.com",
    "https://facebook.com"
)

results = {} #결과를 dicts로 만들어보자!

# for in 반복문 : tuple 혹은 집합체 각각의 item에 대한 코드를 실행 할 수 있다.
for website in websites: #websites tuples에서 item의 갯수만큼 사이클을 돌릴것이고, 각 사이클에서 tuple의 item을 가지고 와 아래의 함수에 대입하여 코드를 실행한다.(item의 갯수만큼)
    print("website is equals to", website) # for 뒤에 붙는 너가 정의한 변수로 item에 접근 할 수 있게 해준다.
    """if website.startswith("https://"): #True or False를 return하는 method를 사용해서 if문을 작성하였다.
        print("good to go")
    else:
        print("we have to fix it")"""
    if not website.startswith("https://"): # not을 사용함으로서   website.startswith("https://") === False 와 같아졌다.
        print("i can fix!")
        website = f"https://{website}"
    print("fix :",website)
    response = get(website) #get function은 response를 return해준다.
    if response.status_code == 200:
        print(f"{website} is OK")
        results[website] = "OK"
    else:
        print(f"{website} not OK")
        results[website] = "FAILED"

print("=====================================================================================================================")
print(results)

"""
request란?
browser을 열어서 주소창에 google.com이라고 입력(request)하면 구글 사이트가 뜬다(response).
위와 같은 request는 파이썬의 내장 함수가 아닌 라이브러리로 따로 다운받아서 사용해야한다.
파이썬을 위한 라이브러리는 다른 사용자도 만들 수 있으며 그 수는 엄청나게 많다.
https://www.pypi.org
"""
