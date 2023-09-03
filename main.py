import numpy as np
import pandas as pd
import pickle
from flask import Flask, render_template, request, request, redirect, url_for


app = Flask(__name__)
model = pickle.load(open('XGBR_model.pkl', 'rb'))

columns = ['Model_Year', 'Division', 'Engine_Displacement', 'Cylinder','Transmission', 
           'Air_Aspiration_Method', 'Transmission_Desc', 'Gears', 'Drive_Desc', 'Fuel_Usage_Desc', 
           'Carline_Class_Desc']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods= ['POST'])
def predict():
    
    # Define the columns used in the model
    cols = ['Model_Year', 'Division', 'Engine_Displacement', 'Cylinder','Transmission', 
           'Air_Aspiration_Method', 'Transmission_Desc', 'Gears', 'Drive_Desc', 'Fuel_Usage_Desc', 
           'Carline_Class_Desc']

    
    # Getting user input   
    
    model_year = int(request.form.get('Model Year'))
    brand = request.form.get("Division")
    engine = float(request.form.get('Engine Displacement'))
    cylinder = int(request.form.get('Cylinder'))
    transmission = request.form.get('Transmission')
    air_aspiration = request.form.get('Air Aspiration Method')
    transmission_desc = request.form.get('Transmission Description')
    gears = int(request.form.get('Gears'))
    drive_desc = request.form.get('Drive Description')
    fuel = request.form.get("Fuel_Usage_Desc")
    carline = request.form.get("Carline_Class_Desc")   
    
    
    # storing the inputs into a numpy array.
    #inputs = np.array([model_year, brand, engine, cylinder, transmission, air_aspiration, transmission_desc,
                     #gears, drive_desc, fuel, carline]).reshape(1,-1)
    
    # Create a DataFrame from user inputs
    user_data = pd.DataFrame(data=[[model_year, brand, engine, cylinder, transmission, air_aspiration,
                                    transmission_desc, gears, drive_desc, fuel, carline]], columns=cols)

    
    # Transforming the data into a dataframe.
    #data = pd.DataFrame(data = inputs, columns= cols)
    
     # Make predictions
    prediction = model.predict(user_data)
    output = round(float(prediction[0]), 2)
    #return render_template("index.html", prediction_text = f'The fuel Economy for {brand} brand type of light_duty vehicle is {output}')
    return redirect(url_for('show_result', 
    prediction_text = f'The fuel Economy for {brand} brand type of light_duty vehicle is {output} Kilometer per Litre'))

@app.route('/result')
def show_result():
    # Get the prediction text from the URL parameter
    prediction_text = request.args.get('prediction_text', 'No prediction available.')
    return render_template('result.html', prediction_text=prediction_text)

# To allow the app to be run on local host for testing and debugging.
if __name__ == '__main__':
    app.run(debug = True)
    

# To allow the app to be run on all IP, which will be used when deploying the app on a server
# if __name__=='__main__':
    #app.run(host = '0.0.0.0', port = 8888)