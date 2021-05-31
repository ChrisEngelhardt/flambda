from flask import Flask
from flask import render_template, request

import os, json

from glob import glob
from LambdaFunction import LambdaFunction

lambdas = {}
app = Flask(__name__)

@app.route("/")
def home():
    routes = [key for key in lambdas.keys()]
    return render_template("list.html",data=routes, url=request.host)

@app.route("/lambda/<lmbd>", methods = ["POST"])
def handler(lmbd):
    arguments = json.loads(request.get_data())
    return lambdas[lmbd].call(arguments)

def register_routes():
    for path in glob("/app/lambdas/*"):
        name = os.path.basename(path)
        print(f"Register handler for {name}")
        lambdas[name]=LambdaFunction.create(path,name)

if __name__ == "__main__":
    register_routes()  
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
