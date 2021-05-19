from flask import Flask
from flask import render_template, request

import os, sys
import json
from glob import glob

lambdas = {}
app = Flask(__name__)

@app.route("/")
def home():
    routes = [key for key in lambdas.keys()]
    return render_template("list.html",data=routes, url=request.host)

@app.route("/lambda/<lmbd>", methods = ["POST"])
def handler(lmbd):
    #my_class = getattr(lambdas[lmbd], lmbd)
    j = json.loads(request.get_data())
    return json.dumps(lambdas[lmbd].main(j))

def register_routes():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    for g in glob("/app/lambdas/*"):
        name = os.path.basename(g)
        print(f"Register handler for {name}")
        sys.path.append(os.path.abspath(os.path.join(BASE_DIR, f'lambdas/{name}')))
        lambdas[name] = __import__(name)

if __name__ == "__main__":
    
    register_routes()  
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
