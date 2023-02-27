from flask import Flask, render_template, request, redirect, send_file
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.file import save_to_file

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
    return render_template("home.html")

# fake DB, 리로드를 하던가 같은 결과를 불러오면 기존에 scrapping한 걸로 대체.
db = {}

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword,db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True) #as_attachment로 다운로드 실행.

app.run("127.0.0.1")
