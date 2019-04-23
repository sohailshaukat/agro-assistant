from flask import Flask, render_template
from soils import soils

app = Flask(__name__)


app.config['SECRET_KEY']='mykey'

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")

@app.route('/sensor_data')
def sensor_data():
    return render_template('sensor_data.html')

@app.route('/weather-prediction')
def weather_prediction():
    return render_template('weather_prediction.html')

@app.route('/soil-guru')
def soil_guru():
    return render_template('soil_guru.html')

@app.route('/soil-guru/alluvial-soil')
def alluvial_soil():
    data = soils.alluvial_soil_data()
    crops = data['crop']
    messages = data['description']
    message_length = len(messages)
    name = data['name']

    return render_template('alluvial-soil.html', crops = crops, messages = messages, message_length = message_length, name = name)
@app.route('/soil-guru/red-soil')
def red_soil():
    data = soils.red_soil_data()
    crops = data['crop']
    messages = data['description']
    message_length = len(messages)
    name = data['name']
    return render_template('red-soil.html', crops = crops, messages = messages, message_length = message_length, name = name)

@app.route('/soil-guru/black-soil')
def black_soil():
    data = soils.black_soil_data()
    crops = data['crop']
    messages = data['description']
    message_length = len(messages)
    name = data['name']
    return render_template('black-soil.html', crops = crops, messages = messages, message_length = message_length, name = name)


@app.route('/soil-guru/mountain-soil')
def mountain_soil():
    data = soils.mountain_soil_data()
    crops = data['crop']
    messages = data['description']
    message_length = len(messages)
    name = data['name']
    return render_template('mountain-soil.html', crops = crops, messages = messages, message_length = message_length, name = name)

@app.route('/soil-guru/laterite-soil')
def laterite_soil():
    data = soils.laterite_soil_data()
    crops = data['crop']
    messages = data['description']
    message_length = len(messages)
    name = data['name']
    return render_template('laterite-soil.html', crops = crops, messages = messages, message_length = message_length, name = name)

@app.route('/soil-guru/desert-soil')
def desert_soil():
    data = soils.desert_soil_data()
    crops = data['crop']
    messages = data['description']
    message_length = len(messages)
    name = data['name']
    return render_template('desert-soil.html', crops = crops, messages = messages, message_length = message_length, name = name)

@app.route('/soil-genie')
def soil_genie():


    return render_template('soil-genie.html')

if __name__ == '__main__':
    app.run(debug = True)
