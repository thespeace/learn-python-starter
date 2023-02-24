from requests import get
from bs4 import BeautifulSoup

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Cant request page")
else:
    print(response.text)
