#Binomial Calculator
from tkinter import *
from tkinter import messagebox
from math import pow as pow
from math import comb as comb
class BiCalc:
	def __init__(self):
		window = Tk()
		window.title("Binomial distribution probability calculator")
		window.geometry("500x500")
		#input
		Label(window, text="p",
			font ="Helvetica 16").grid(row=1,column=1,sticky=W)
		Label(window, text="n",
			font ="Helvetica 16").grid(row=2,column=1,sticky=W)
		Label(window, text="start",
			font ="Helvetica 16").grid(row=3,column=1,sticky=W)
		Label(window, text="stop",
			font ="Helvetica 16").grid(row=4,column=1,sticky=W)
		Label(window, text= None).grid(row=5,column=1,sticky=W)
		#Output
		Label(window, text="Probability").grid(row=6,column=1,sticky=W)
		Button(window, text="Calculate Prob",
			command=self.calcProb, 
			font="Helvetica 14").grid(row=7,column=2,padx=(100,5),pady=5)

		self.p = StringVar()
		self.n = StringVar()
		self.i = StringVar()
		self.r = StringVar()
		self.prob = StringVar()
		self.status = StringVar()

		Entry(window, textvariable= self.p,
			justify=RIGHT).grid(row=1,column=2,sticky=E)
		Entry(window, textvariable=self.n,
			justify=RIGHT).grid(row=2,column=2,sticky=E)
		Entry(window, textvariable=self.i,
			justify=RIGHT).grid(row=3,column=2,sticky=E)
		Entry(window, textvariable=self.r,
			justify=RIGHT).grid(row=4,column=2,sticky=E)

		Label(window, textvariable=self.prob,
			font = "Helvetica 18 bold",
			justify=RIGHT).grid(row=6,column=2,sticky=E)

		if self.status=="1":
			messagebox.showalert(title="ERROR",message="r can't be bigger than n")
		window.mainloop()

	def calcProb(self):
		p = float(self.p.get())
		q = 1-p
		n = int(self.n.get())
		i = int(self.i.get())
		r = int(self.r.get())
		prob = 0

		if (r-n>0):
			self.prob.set("ERROR : PLEASE TRY AGAIN")
			self.status.set("1")

		
		for ii in range(i,r+1):
			prob += comb(n,ii)*pow(p,ii)*pow(q,n-ii)
		self.prob.set(format(prob,"5,.5f"))



BiCalc()		