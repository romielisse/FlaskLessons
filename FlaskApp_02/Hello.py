# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
   favorite = "Jon Snow"
   others = ["Danny", "The hound", "Arya", "Night King"]
   return render_template("index.html", 
							favorite_character = favorite, 
							other_characters = others)

if __name__ == '__main__':
   app.run()