from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_experimental_option("detach", True) #브라우저 꺼짐 방지 코드
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) #불필요한 에러 메시지 삭제

service = Service(executable_path= ChromeDriverManager().install()) # 크롬 드라이버 최신 버전 자동 설치 후 서비스 만들기

browser = webdriver.Chrome(service = service, options = chrome_options) #크롬드라이버를 최신으로 유지해줍니다.

def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs"
    final_url = f'{base_url}?q={keyword}&start={99999}'
    response = browser.get(final_url)
    soup = BeautifulSoup(browser.page_source,"html.parser")
    last_page = (soup.find('nav',role='navigation'))
    count = last_page.select('div a')
    pages = int(count[-1]['aria-label']) + 1
    print(pages)
    return pages

    # pages = pagination.find_all("li", recursive=False) #bs4에게 바로 아래에 있는 것들만 검색하고 그 자식 요소들까지는 검색하지 말라고 말해줌.
def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results=[]
    for page in range(pages): # range ? 받은 인자를 가지고 숫자 배열을 만들어준다. ex) for i in range(5): print(i) >> 0 1 2 3 4
        base_url = "https://kr.indeed.com/jobs"
        final_url = f'{base_url}?q={keyword}&start={page*10}'
        browser.get(final_url)
        print("Requesting", final_url)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all('li', recursive=False)

        print("개수 : ",len(jobs))
        for job in jobs:
            zone = job.find("div", class_="mosaic-zone") #li들 중에 class="mosaic-zone"인 div를 찾아 제거하기 위해 사용.
            if zone == None: #찾지 못하였다는 그건 직업을 가지고 있는 li여서 우리가 데이터 수집 가능.
                anchor = job.select_one("h2 a")
                title = anchor['aria-label'] # aria-label : 화면 리더기가 읽게 하길 원하는 텍스트를 포함시켜 준다. ex) 시각장애인을 위해 페이지를 읽어주도록 하기 위함.
                # 우리가 찾은 html element들의 속성의 테이터구조를 bs4를 사용해 list와 dictionary로 변환시켜 받을 수 있다.
                link = anchor['href']
                company = job.find("span",class_="companyName")
                location = job.find("div",class_="companyLocation")
                job_data = {
                    'link' : f"https://kr.indeed.com{link}",
                    'company' : company.string.replace(","," "),
                    'location' : location.string.replace(","," "),
                    'position' : title.replace(","," "),
                }
                results.append(job_data)
        for result in results:
            print(result)
    return results

"""
None? 데이터 타입중 하나로, 무언가가 있어야 하는데 없다고 나타내준다. False와는 다르다.(false는 true가 아닐때를 뜻한다)
"""
