from flask import Flask, render_template, request, redirect, url_for, flash  



app = Flask(__name__, instance_relative_config=True)




@app.route('/')
def home():
	return render_template("home.html")




@app.route('/about')
def about():
	return render_template("about.html")



