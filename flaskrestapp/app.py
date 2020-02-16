from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores ={
		'FirstStore':
					{'ItemA': 200, 'ItemB': 300},
		'SecondStore':
					{'ItemC': 200, 'ItemD': 300}
		}

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

@app.route('/stores/<string:name>', methods = ['GET'])
def get_store(name):
	if name in stores.keys():
		return jsonify(stores.get(name))
	else:
		return{"message":"Invalid Key"}


@app.route("/stores/<string:item>", methods=['POST'])#new item added in existing store
def add_item(item):
	request_data = request.get_json()
	if item in  stores.keys():
		stores.get(item).update(request_data)
		return{"message":"item added to store"}
	else:
		return{"message":"Invalid store"}


@app.route('/stores', methods = ['POST'])#new store created
def create_store():
	request_data = request.get_json()
	#new_store = {
				#'name': request_data['name'],
				#'item': []
				#}
	#stores.append(new_store) #to append json data in list
	stores.update(request_data) # update data in dictionary send from postman
	#return jsonify(new_store)
	return{"message":"store created"}


app.run(port = 5000)