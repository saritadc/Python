from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

stores = [] #empty store initialized in memory
class Store(Resource):
	def get(self,name):
		for store in stores:
			if store['name']== name:
				return{"store":store}, 200
			else:
				return{"message": "{} not found".format(name)},404
		return {"message":"This is simple get request"}

	def post(self,name):
		data = request.get_json()
		for store in stores:
			if store['name'] == name:
				return{"message":"{} already exists".format(name)}
		store = {'name': name, 'address': data['address'], 'employees': data["employees"]}
		stores.append(store)
		return{"message":"succesfully created store {}".format(name)}, 201

	def put(self,name):
		data = request.get_json()
		for store in stores:
			if store['name'] == name:
				store.update(data)
				return{"message":"{} already exists so updating..".format(name)}
		store = {'name': name, 'address': data['address'], 'employees': data["employees"]}
		stores.append(store)
		return{"message":"succesfully created store {}".format(name)}, 201

	def delete(self,name):
		for store in stores:
			if store['name']!= name:
				return{"message":"{} not found"}, 404


class StoreList(Resource):
	def get(self):
		return {'stores' : stores}


api.add_resource(Store,"/store/<string:name>/")
api.add_resource(StoreList,"/stores")

app.run(port=5000)