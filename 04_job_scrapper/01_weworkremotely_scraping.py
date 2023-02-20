# https://weworkremotely.com/
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python" #해당변수로 스크래핑할 대상을 지정.

response = get(f"{base_url}{search_term}")
# print(response) #200 sucess 확인!
if response.status_code != 200: #예외처리
    print("Can't request website")
else:
    results = [] #***********크롤링 한 결과를 dictionary에 저장하기 위한 빈 배열 선언.
    # print(response.text) #웹 사이트를 구성하고 있는 코드 확인.
    soup = BeautifulSoup(response.text, "html.parser") #html코드(response.text)를 우리가 다룰 수 있는 python entity(데이터 구조)로 변환해준다. string뿐만 아니라 실제 python 데이터 구조로 이용할 수 있다.
    # print(soup.find_all('title'))
    jobs = soup.find_all('section', class_="jobs") # class_ 는 keyword argument! 맨 아래의 주석 안의 예를 통해 살펴보자.
                                                   # find_all은 엄청나게 많은 argument들을 가지고 있기 때문에 키워드로 인자를 지정해줬다.
                                                   # 그리고 class 뒤에 _ 해당 기호를 붙인이유는 이미 파이썬이 class를 점유하고있기때문이다.
                                                   # find_all은 항상 list를 리턴한다.
    # print(len(jobs)) #jobs 클래스를 가진 section을 몇 개 받았는지 확인해보자.
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1) #list의 마지막 항목 제거, remove "view-all"
        for post in job_posts:
            anchors = post.find_all('a')
            anchor = anchors[1]
            link = anchor['href'] #bs4는 가져온 모든 html을 dictionary로 바꿔준다. 때문에 키(속성)를 입력하면 값이 나온다.
            company, kind, region = anchor.find_all('span', class_="company")
            title = anchor.find('span', class_='title')
            # print(company.string, kind.string, region.string, title.string) # .string 메소드를 통해 태그들을 없애고 문자열만 가져와보자.
            # print("============================================================")
            job_data = {
                'link' : f"https://weworkremotely.com{link}",
                'company' : company.string,
                'region' : region.string,
                'position' : title.string
            }
            results.append(job_data)
    # print(results) # 크롤링의 결과값을 dictionary로 가득 찬 list로 완성!
    for result in results:
        print(result)
"""
def say_hello(name, age):
    print(f"Hello {name} you are {age} years old")

position argument
say_hello("seo", 12) # 해당 인자의 위치에 따라 해당 함수의 매개변수값으로 받는 걸 position argument라 한다.

keyword argument
say_hello(age=12 , name="seo") #위치(순서)를 무시하고 argument를 기입하는 형식으로 사용할 수 있 다.
"""

""" list의 각 요소의 변수를 빠르고 쉽게 만들기.
list_of_number = [1,2,3] 
first , second, third = list_of_number

print(first,second,third)
"""