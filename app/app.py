from flask import Flask, request
import json 

app = Flask(__name__)

#API ROUTE
@app.route("/")
def hello_world():
    return {"result": f"Hello World!"}