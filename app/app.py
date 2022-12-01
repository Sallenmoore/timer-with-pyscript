from flask import Flask, request, render_template
import json 

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

#API ROUTE
@app.route("/")
def index():
    return render_template('index.html')