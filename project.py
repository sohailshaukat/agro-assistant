from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField, SelectField,
                    TextField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired
from soils import soils,advice
from rainfall_prediction import rainfall_regressor

app = Flask(__name__)


app.config['SECRET_KEY']='mykey'

class GenieSoilForm(FlaskForm):

    soil_type = SelectField(u'Select a Soil type:',choices = [('soil_type_null','Null'),('soil_type_alluvial','Alluvial'),('soil_type_red','Red'),
                                                            ('soil_type_black','Black'),('soil_type_mountain','Mountain'),
                                                            ('soil_type_laterite','Laterite'),('soil_type_desert','Desert')])
    submit = SubmitField('Submit')

class GenieCropForm(FlaskForm):

    crop_option = SelectField(u'Select a Crop kind:', choices =[('crop_option_null','Null'),('crop_option_rice','Rice'),('crop_option_wheat','Wheat'),
                                                                ('crop_option_sugarcane','Sugarcane'),('crop_option_groundnut','Groundnut'),
                                                                ('crop_option_apple','Apple'),('crop_option_strawberry','Strawberry'),
                                                                ('crop_option_maize','Maize'),('crop_option_grapes','Grapes'),('crop_option_coffee','Coffee')])
    submit = SubmitField('Submit')

class GenieFertilizerForm(FlaskForm):

    soil_type = SelectField(u'Select a Soil type:',choices = [('soil_type_null','Null'),('soil_type_alluvial','Alluvial'),('soil_type_red','Red'),
                                                            ('soil_type_black','Black'),('soil_type_mountain','Mountain'),
                                                            ('soil_type_laterite','Laterite'),('soil_type_desert','Desert')])

    crop_option = SelectField(u'Select a Crop kind:', choices =[('crop_option_null','Null'),('crop_option_rice','Rice'),('crop_option_wheat','Wheat'),
                                                                ('crop_option_sugarcane','Sugarcane'),('crop_option_groundnut','Groundnut'),
                                                                ('crop_option_apple','Apple'),('crop_option_strawberry','Strawberry'),
                                                                ('crop_option_maize','Maize'),('crop_option_grapes','Grapes'),('crop_option_coffee','Coffee')])

    submit = SubmitField('Request')



@app.route('/',methods=['GET','POST'])
def index():
    return render_template("home.html")

@app.route('/about-and-download')
def about():
    return render_template("about.html")

@app.route('/sensor_data')
def sensor_data():
    return render_template('sensor_data.html')

@app.route('/rainfall-prediction/graphs')
def rainfall_prediction_graph():
    return render_template('rainfall-prediction-graphs.html')

@app.route('/rainfall-prediction')
def rainfall_prediction():
    rainfall_data_tuple = rainfall_regressor.rain_predictor()
    june_pred_linear = rainfall_data_tuple[0]['June']
    july_pred_linear = rainfall_data_tuple[0]['July']
    august_pred_linear = rainfall_data_tuple[0]['August']
    september_pred_linear = rainfall_data_tuple[0]['September']
    october_pred_linear = rainfall_data_tuple[0]['October']

    june_pred_polynomial = rainfall_data_tuple[1]['June']
    july_pred_polynomial = rainfall_data_tuple[1]['July']
    august_pred_polynomial = rainfall_data_tuple[1]['August']
    september_pred_polynomial = rainfall_data_tuple[1]['September']
    october_pred_polynomial = rainfall_data_tuple[1]['October']

    return render_template('rainfall_prediction.html', august_pred_linear = august_pred_linear , september_pred_linear = september_pred_linear, october_pred_linear = october_pred_linear , june_pred_linear = june_pred_linear, july_pred_linear = july_pred_linear,
                            june_pred_polynomial = june_pred_polynomial, july_pred_polynomial = july_pred_polynomial, august_pred_polynomial = august_pred_polynomial, september_pred_polynomial = september_pred_polynomial, october_pred_polynomial = october_pred_polynomial)

@app.route('/agro-guru')
def soil_guru():
    return render_template('soil_guru.html')

@app.route('/agro-guru/alluvial-soil')
def alluvial_soil():
    data = soils.alluvial_soil_data()
    crops = data['crop']
    messages = data['description']
    message_length = len(messages)
    name = data['name']

    return render_template('alluvial-soil.html', crops = crops, messages = messages, message_length = message_length, name = name)
@app.route('/agro-guru/red-soil')
def red_soil():
    data = soils.red_soil_data()
    crops = data['crop']
    messages = data['description']
    message_length = len(messages)
    name = data['name']
    return render_template('red-soil.html', crops = crops, messages = messages, message_length = message_length, name = name)

@app.route('/agro-guru/black-soil')
def black_soil():
    data = soils.black_soil_data()
    crops = data['crop']
    messages = data['description']
    message_length = len(messages)
    name = data['name']
    return render_template('black-soil.html', crops = crops, messages = messages, message_length = message_length, name = name)


@app.route('/agro-guru/mountain-soil')
def mountain_soil():
    data = soils.mountain_soil_data()
    crops = data['crop']
    messages = data['description']
    message_length = len(messages)
    name = data['name']
    return render_template('mountain-soil.html', crops = crops, messages = messages, message_length = message_length, name = name)

@app.route('/agro-guru/laterite-soil')
def laterite_soil():
    data = soils.laterite_soil_data()
    crops = data['crop']
    messages = data['description']
    message_length = len(messages)
    name = data['name']
    return render_template('laterite-soil.html', crops = crops, messages = messages, message_length = message_length, name = name)

@app.route('/agro-guru/desert-soil')
def desert_soil():
    data = soils.desert_soil_data()
    crops = data['crop']
    messages = data['description']
    message_length = len(messages)
    name = data['name']
    return render_template('desert-soil.html', crops = crops, messages = messages, message_length = message_length, name = name)

@app.route('/agro-genie',methods=['GET','POST'])
def soil_genie():
    form_soil = GenieSoilForm()
    form_crop = GenieCropForm()
    form_fertilizer = GenieFertilizerForm()
    session['formtype'] = False
    if form_fertilizer.validate_on_submit():
        session['soil_type'] = form_fertilizer.soil_type.data
        session['crop_option'] = form_fertilizer.crop_option.data
        session['formtype'] = 'fertilizer_genie'
        return redirect(url_for('soil_genie_result'))
    if form_soil.validate_on_submit():
        session['soil_type'] = form_soil.soil_type.data
        session['formtype'] = 'soil_genie'
        return redirect(url_for('soil_genie_result'))
    elif form_crop.validate_on_submit():
        session['crop_option'] = form_crop.crop_option.data
        session['formtype'] = 'crop_genie'
        return redirect(url_for('soil_genie_result'))


    return render_template('soil-genie.html', form_soil = form_soil , form_crop = form_crop,form_fertilizer = form_fertilizer)


@app.route('/agro-genie/advice')
def soil_genie_result():
    soil_type_result = False
    crop_list = False
    soil_list = False
    crop_option_result = False
    messages_advice = False
    points_advice = False
    compatibility_string = False
    form_type = 'NoForm'

    if not session['formtype']:
        pass
    elif session['formtype'] == 'soil_genie':
        data_publish = soils.soil_to_crop(session['soil_type'])
        soil_type_result = data_publish['soil_type']
        crop_list = data_publish['crop_list']
        form_type = 'soil_genie'
        pass
    elif session['formtype'] == 'crop_genie':
        data_publish = soils.crop_to_soil(session['crop_option'])
        soil_list = data_publish['soil_list']
        crop_option_result = data_publish['crop_option_result']
        form_type = 'crop_genie'
        pass
    elif session['formtype'] == 'fertilizer_genie':
        data_publish_fertilizer = advice.advice(session['soil_type'], session['crop_option'])
        messages_advice = data_publish_fertilizer['advice_messages']
        points_advice = data_publish_fertilizer['advice_points']
        soil_type_result = data_publish_fertilizer['soil_type']
        crop_option_result = data_publish_fertilizer['crop_option']
        compatibility_string = data_publish_fertilizer['compatibility']
        form_type = 'fertilizer_genie'
        pass
    return render_template('soil-genie-advice.html',form_type = form_type,soil_type_result= soil_type_result, crop_list= crop_list, crop_option_result = crop_option_result , soil_list =soil_list , messages_advice = messages_advice , points_advice = points_advice, compatibility_string = compatibility_string )




@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug = True)
