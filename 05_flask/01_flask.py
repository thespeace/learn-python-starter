from flask import Flask, render_template, request
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask("JobScrapper")

"""@app.route("/") #decorator, 함수 위에 위치시켜야 한다. 아래의 함수를 decorating하고 있을 때만 동작한다.
def home(): #systactic sugar
    return render_template("home.html", name="seo") #html파일에 변수인 name 보내기.

@app.route("/hello")
def hello():
    return 'hello you!'
"""

@app.route("/")
def home():
    return render_template("home.html")\

db = {}

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("127.0.0.1")
