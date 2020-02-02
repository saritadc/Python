from flask import Flask, jsonify, request, render_template

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
	return render_template("index.html")

@app.route('/maps')
def maps():
	return "I am on google maps."

@app.route("/stores", methods = ['GET'])
def get_stores():
	return jsonify(stores)

@app.route('/stores', methods = ['POST'])
def create_store():
	request_data = request.get_json()
	new_store = {
				'name': request_data['name'],
				'item': []
				}
	stores.append(new_store)
	return jsonify(new_store)

app.run(port = 5000)