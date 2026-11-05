from flask import Flask,jsonify ;
from flask_cors import CORS ;

app = Flask(__name__)
CORS(app)
@app.route("/api/home",methods=['GET'])
def return_home():
        return jsonify({
            'msg':"Find your next colocation",
            'welcomeMsg':"Find people looking to share home , based on location ,budget and prefrences"
           
        })
@app.route("/api/about",methods=['GET'])   
def return_aboout():
    return jsonify({
       'title':"من نحن",
       'description':"App Yara this qpp for reservation Hotel ",
       'version':"1.0.0"
    })    
if __name__ == "__main__":
    app.run(debug=True, port=5000)