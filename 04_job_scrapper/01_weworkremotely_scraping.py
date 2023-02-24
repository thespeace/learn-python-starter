# https://weworkremotely.com/
from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs #refactoring and function import

jobs = extract_wwr_jobs("python")
print(jobs)
