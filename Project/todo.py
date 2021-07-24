from flask import Flask
from flask import render_template

app=Flask('Todoapp')

@app.route("/")

def func():
    return render_template("todolist.html")


if __name__=="__main__":
	app.run()
