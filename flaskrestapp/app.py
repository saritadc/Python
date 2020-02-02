from flask import Flask, jsonify

app = Flask(__name__)

stores = [{ 
		'names': 'FirstStore',
		'items': [{'name':'IteamA', 'price': 200}, {'name': 'IteamB', 'price': 300}]
		},
		{
		'name': 'SecondStore',
		'items':[{'name': 'IteamC', 'price': 300}]
		}]

#https://www.google.com/

@app.route('/') #@ is decorator for method
def home():
	return"Hello World!"

@app.route('/maps')
def maps():
	return "I am onm google maps."

@app.route("/stores", methods = ['GET'])
def get_stores():
	return jsonify(stores)

@app.route('/stores', methods = ['POST'])
def create_store():
	pass

app.run(port = 5000)