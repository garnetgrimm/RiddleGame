from flask import Flask
import random
from flask import jsonify
import os
from flask import render_template
from flask import request

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

#the below 3 lines simply causes only errors and print statements to be logged to console
#otherwise every freaking request will be logged
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__, static_url_path = "", static_folder = "static")

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/pboat287')
def pboat():
	return render_template("pboat287.html")

@app.route('/ecar563')
def ecar():
	return render_template("ecar563.html")

@app.route('/tryPBOAT', methods = ['POST'])
def tryPboat():

	s1 = request.form.get('s1')
	s2 = request.form.get('s2')
	
	r = False
	
	if(s1 == "19O" and s2 == "25O"):
		r = True
	elif(s1 == "25O" and s2 == "19O"):
		r = True
	else:
		r = False
	
	response = jsonify(r)
	response.headers.add('Access-Control-Allow-Origin', '*')	
	return response
	
@app.route('/tryECAR', methods = ['POST'])
def tryEcar():

	s1 = request.form.get('s1')
	
	r = False
	
	if(s1 == "c"):
		r = True
	if(s1 == "C"):
		r = True
	
	
	response = jsonify(r)
	response.headers.add('Access-Control-Allow-Origin', '*')	
	return response

