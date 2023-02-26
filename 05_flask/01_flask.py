from flask import Flask

app = Flask("JobScrapper")

@app.route("/") #decorator, 함수 위에 위치시켜야 한다. 아래의 함수를 decorating하고 있을 때만 동작한다.
def home(): #systactic sugar
    return 'hey there!'

app.run("127.0.0.1")