from tkinter import *
from flask import Flask,redirect, url_for,render_template,request
import os

def d_dtcn():
	root = Tk()
	root.configure(background = "grey")

	def function1(): 
		os.system("python drowsiness_detection.py --shape_predictor shape_predictor_68_face_landmarks.dat")
		exit()
    
	def function2(): 
		os.system("python android_cam.py --shape_predictor shape_predictor_68_face_landmarks.dat")
		exit()

	
		
	root.title("DROWSINESS DETECTION SYSTEM")
	Button(root,text="TEST WITH WEBCAM",font=("times new roman",20),bg="white",fg='black',height=8,command=function1).grid(row=2,columnspan=3,sticky=W+E+N+S,padx=25,pady=25)
	Button(root,text="TEST WITH ANDROID",font=("times new roman",20),bg="white",fg='black',command=function2).grid(row=5,columnspan=3,sticky=W+E+N+S,padx=25,pady=25)
	Button(root,text="STOP TESTING",font=("times new roman",20),bg="white",fg='black',height=8,command=root.destroy).grid(row=7,columnspan=3,sticky=W+E+N+S,padx=25,pady=25)

	root.mainloop()