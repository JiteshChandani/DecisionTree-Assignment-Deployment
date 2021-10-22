from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle

app = Flask(__name__, template_folder= 'Template') # initializing a flask app
#app=application
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
            Age= float(request.form['Age'])
            Fare = float(request.form['Fare'])
            Parch = int(request.form['Parch'])
            Pclass = int(request.form['Pclass'])
            Sex = int(request.form['Sex'])
            SibSp = int(request.form['SibSp'])

            filename = 'decision_tree.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict([[Age,Fare,Parch,Pclass,Sex,SibSp ]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction= prediction)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
            # return render_template('results.html')
        else:
            return render_template('index.html')

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True,port = 5001) # running the app

