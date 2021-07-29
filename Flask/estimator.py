import random


def estimatepi_monte(var):
	inside=0
	for i in range(var):
		x=random.random()
		y=random.random()
		if (x**2 +y**2) <=1:
			inside+=1
	pival=4*inside/var
	return pival


def estimatepi_Wallis(var):
	acc=1
	for n in range(1,var+1):
		acc=acc*(4*n**2)/(4*n**2-1)
	pival=acc*2
	return pival
