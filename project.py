from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField, SelectField,
                    TextField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired
from soils import soils

app = Flask(__name__)


app.config['SECRET_KEY']='mykey'

class GenieSoilForm(FlaskForm):

    soil_type = SelectField(u'Select a Soil type:',choices = [('soil_type_alluvial','Alluvial'),('soil_type_red','Red'),
                                                            ('soil_type_black','Black'),('soil_type_mountain','Mountain'),
                                                            ('soil_type_laterite','Laterite'),('soil_type_desert','Desert')])
    submit = SubmitField('Submit')

class GenieCropForm(FlaskForm):

    crop_option = SelectField(u'Select a Crop kind:', choices =[('crop_option_rice','Rice'),('crop_option_wheat','Wheat'),
                                                                ('crop_option_sugarcane','Sugarcane'),('crop_option_groundnut','Groundnut'),
                                                                ('crop_option_apple','Apple'),('crop_option_strawberry','Strawberry'),
                                                                ('crop_option_maize','Maize'),('crop_option_grapes','Grapes'),('crop_option_coffee','Coffee'),
                                                                ('crop_option_pulses','Pulses')])
    submit = SubmitField('Submit')

class GenieFertilizerForm(FlaskForm):

    soil_type = SelectField(u'Select a Soil type:',choices = [('soil_type_alluvial','Alluvial'),('soil_type_red','Red'),
                                                            ('soil_type_black','Black'),('soil_type_mountain','Mountain'),
                                                            ('soil_type_laterite','Laterite'),('soil_type_desert','Desert')])

    crop_option = SelectField(u'Select a Crop kind:', choices =[('crop_option_rice','Rice'),('crop_option_wheat','Wheat'),
                                                                ('crop_option_sugarcane','Sugarcane'),('crop_option_groundnut','Groundnut'),
                                                                ('crop_option_apple','Apple'),('crop_option_strawberry','Strawberry'),
                                                                ('crop_option_maize','Maize'),('crop_option_grapes','Grapes'),('crop_option_coffee','Coffee'),
                                                                ('crop_option_pulses','Pulses')])

    submit = SubmitField('Submit')



@app.route('/',methods=['GET','POST'])
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

@app.route('/soil-genie',methods=['GET','POST'])
def soil_genie():
    form_soil = GenieSoilForm()
    form_crop = GenieCropForm()
    form_fertilizer = GenieFertilizerForm()
    if form_soil.validate_on_submit():
        session['soil_type'] = form_soil.soil_type.data
        return redirect(url_for('soil_genie_result'))
    elif form_crop.validate_on_submit():
        session['crop_option'] = form_crop.crop_option.data
        return redirect(url_for('soil_genie_result'))
    elif form_fertilizer.validate_on_submit():
        session['soil_type'] = form_fertilizer.soil_type.data
        session['crop_option'] = form_fertilizer.crop_option.data
        return redirect(url_for('soil_genie_result'))



    return render_template('soil-genie.html',form_soil = form_soil, form_crop = form_crop, form_fertilizer = form_fertilizer)

@app.route('/soil-genie/advice')
def soil_genie_result():
    return render_template('soil-genie-advice.html')

if __name__ == '__main__':
    app.run(debug = True)
