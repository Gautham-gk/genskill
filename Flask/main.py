from flask import Flask
import random
from flask import render_template

app=Flask("Genskill")


@app.route("/pi")

def estimatepi_monte(var=15000):
	inside=0
	for i in range(var):
		x=random.random()
		y=random.random()
		if (x**2 +y**2) <=1:
			inside+=1
	estimate=4*inside/var
	return  render_template("estimate.html",
	algorithm="Monte Carlo",
	var=var,
	estimate=estimate)

@app.route("/pi2")

def estimatepi_Wallis(var=1000):
	acc=1
	for n in range(1,var+1):
		acc=acc*(4*n**2)/(4*n**2-1)
	acc=acc*2
	return render_template("estimate.html",
	algorithm="Wallis",
	var=var,
	estimate=acc)


@app.route("/")

def Hello():
	return render_template("index.html")



if __name__=="__main__":
	app.run()
