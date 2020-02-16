from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route('/request') #@ is decorator for method
def home():
	response = requests.get("http://127.0.0.1:5000/stores")
	print(response.json())
	return render_template("index.html")

app.run(port=5001)