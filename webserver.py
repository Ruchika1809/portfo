from flask import Flask
from flask import render_template, request,redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/work.html")
def work():
    return render_template('work.html')

@app.route("/.html")
def works():
    return render_template('works.html')

@app.route("/<string:page_name>")
def call_page(page_name):
    return render_template(page_name)

def add_data(data):
    with open('database.txt',mode='a') as db:
        email=data["email"]
        subject=data["subject"]
        text=data["text"]
        file=db.write(f"\n{email}{subject}{text}")

@app.route("/submitForm",methods=['POST','GET'])
def submiForm():
    if request.method=='POST':
        data=request.form.to_dict()
        add_data(data)
        return redirect('/Thankyou.html')
    else:
        return "something went wrong. Please try again!"









