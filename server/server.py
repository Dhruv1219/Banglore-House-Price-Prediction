from flask import Flask ,request,jsonify
from flask_cors import CORS

import util
app=Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/get_location_names')
def get_location_names():
    print("calledd")
    response = jsonify({
        "locations":util.get_location_names()
    })
    # response.headers.add("Acess-Control-Allow-Origin","*")
    return response

@app.route("/predict_home_price",methods=["GET",'POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    response=jsonify({
        "estimated_price":util.get_estimated_price(location,bath,bhk,total_sqft)
    })
    # response.headers.add('Acsess-Control-Allow-Origin',"*")
    return response

if __name__=="__main__":
    print("starting python flask server")
    util.load_saved_artifacts()
    print("Server startup completed")
    app.run()