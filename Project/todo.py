from flask import Flask
from flask import render_template
from flask_moment import Moment

app=Flask(__name__)
moment = Moment(app)


@app.route("/", methods=['GET','POST'])
@app.route("/add.html",methods=['GET','POST'])

def func():
    return render_template("add.html")


@app.route("/updatelist.html",methods=['GET','POST'])
def update():
    return render_template("updatelist.html");



if __name__=="__main__":
    app.run()
