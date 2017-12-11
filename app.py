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
def hello_world():
	return render_template("pboat827.html")

@app.route('/trySolutions', methods = ['POST'])
def trySolutions():

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

