from flask import Flask , request , redirect , render_template
from flask import url_for
from utils import *
app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def index():
    if request.method=="POST":
        print(request.form)
        total_sqft = request.form["total_sqft"]
        location = request.form["location"]
        bhk = request.form["bhk"]
        bath = request.form["bath"]
        return str(get_prediction(location , total_sqft,bath ,bhk))
        
    else:
        return (render_template('index.html'))






if __name__=='__main__':
    app.run(debug=True)