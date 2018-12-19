from flask import Flask, render_template

import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>서버가 html도 보내주나?</h1>"
    
@app.route("/html_tag") #url뒤에 추가해주면 아래의 새로운 정보가 나옴
def html_tag():
    return """
    <h1>첫번째 줄!!!</h1>
    <h2>두번째 줄!!!</h2>
    """
    
@app.route("/html_file")
def html_file():
    return render_template("html_file.html")
    
@app.route("/welcome/<string:name>") #string:name 부분에는 어떠한 문장도 들어올 수 있다는 경우를 열어놓음
def welcome(name):
    return render_template("welcome.html", people=name) #welcome.html에서 people을 사용할수있음

@app.route("/cube/<int:num>")
def cube(num):
    triple = num*num*num
    return render_template("cube.html", triple=triple,num=num) #triple이라는 데이터를 cube.html안에서만 사용할 수 있는 triple에 담아줌 + 또 다른 num (html=python)
    
@app.route("/lunch")
def lunch():
    menu = ["볶음밥", "떡볶이", "라면", "라볶이", "김밥", "국밥", "치킨"]
    pick = random.choice(menu)
    return render_template("lunch.html", pick=pick)
    
@app.route("/lotto")
def lotto():
   numbers = list(range(1,100))
   a = random.sample(numbers,6)
   sort_a = sorted(a) #정렬하기 위해
   return render_template("lotto.html",sort_a=sort_a)
   
@app.route('/naver')
def naver():
    return render_template("naver.html")
    
@app.route('/google')
def google():
    return render_template("google.html")