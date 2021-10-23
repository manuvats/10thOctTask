
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle
from sklearn.ensemble import BaggingClassifier

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            time=float(request.form['time'])
            acc_frontal_axis = float(request.form['acc_frontal_axis'])
            acc_vertical_axis = float(request.form['acc_vertical_axis'])
            acc_lateral_axis = float(request.form['acc_lateral_axis'])
            frequency = float(request.form['frequency'])
            rssi = float(request.form['rssi'])
            phase = float(request.form['phase'])
            antenna_id = float(request.form['antenna_id'])
            room = float(request.form['room'])
            gender = float(request.form['gender'])
            filename = 'DT_Bagging.pkl'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[time,acc_frontal_axis,acc_vertical_axis,acc_lateral_axis,frequency,rssi,phase,antenna_id,room,gender]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=prediction)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app