from requests import get
# from bs4 import BeautifulSoup
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True) #브라우저 꺼짐 방지 코드

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_options) #크롬드라이버를 최신으로 유지해줍니다.

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Cant request page")
else:
    print(response.text)
