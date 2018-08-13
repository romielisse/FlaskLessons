# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def start():
   # return 'Hello World'
   favorite = "Jon Snow"
   others = ["Danny", "The hound", "Arya", "Night King"]
   return render_template("index.html", 
							favorite_character = favorite, 
							other_characters = others)
   
@app.route('/loadform')
def login():
	return render_template("login.html")
	
@app.route('/processform', methods=['POST'])
def processform():
	user = request.form['user']
	return render_template("index.html", username = user)

if __name__ == '__main__':
   app.run()