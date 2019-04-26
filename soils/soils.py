class Soil():

    def __init__(self, crops_grown, description):
        self.crops_grown = crops_grown
        self.description = description


def alluvial_soil_data():
    s1='In India, alluvial soils mainly found in the Indo-Ganga­ Brahmaputra Plains, Coastal Plains and the broad river valleys of South India. Along the river basins of some plateau and mountain regions also found the alluvial oil.'
    s2='In the Indo-Ganga plain, two other types of alluvium found. The old alluviums are clayey and sticky, have a darker color, contain nodules of lime concretions and are found to lie on slightly elevated lands. The new alluviums are lighter in color and occur in the deltas and the flood plains.'
    s3='When compare to the soil into the old alluvial soil and new alluvial soil then found the new alluvial soil is very fertile. Alluvial soil is the abundant harvest and high fertility that’s why it is the best soil of India'
    desc=[s1,s2,s3]

    alluvial = Soil(crops_grown=['Rice','Wheat','Sugarcane','Jute Oilseeds','Pulses'],description = desc)

    data = {'crop': alluvial.crops_grown, 'description': desc, 'name':'Alluvial Soil'}
    return data

def black_soil_data():
    s1 ='The natural or black soils have developed extensively upon the Lava Plateaus of Maharashtra, Gujarat, Madhya Pradesh mainly Malwa. Black soils have also drawn upon gneisses of North Karnataka and north and west of Andhra Pradesh.'
    s2 = 'These soils are very fertile and contain a high percentage of lime and a moderate amount of potash. The type of soil has especially suited the cultivation of cotton.'
    desc = [s1,s2]
    black = Soil(crops_grown=['Sugarcane', 'Wheat','Groundnut'], description=desc)
    data = {'crop': black.crops_grown, 'description': desc, 'name':'Black Soil'}
    return data

def red_soil_data():
    s1 = 'These soils are friable and medium fertile and found mainly in almost whole of Tamil Nadu, South-eastern Karnataka, North-eastern and South-eastern Madhya Pradesh, Jharkhand the major parts of Orissa, and the Hills and Plateaus of North-east India. But these have the capacity to grow good crops after taking help of irrigation and fertilizers.'
    desc = [s1]
    red = Soil(crops_grown=['Wheat','Rice','Millets','Gram','Pulses','Oilseeds','Cotton'],description=desc)
    data = {'crop': red.crops_grown, 'description': desc, 'name':'Red Soil'}
    return data

def mountain_soil_data():
    s1 = 'This soil is rich in humus but deficient in potash, phosphorus, and lime. It is heterogeneous in nature and varies from place to place. The mountain soil is sandy with gravels and is porous.'
    s2 = 'The mountain soil found on the hill slopes covered with forests. In the Himalayan region, such soil mainly found in the valley basins, the depressions, and the lesser steep slopes. The north-facing slopes support soil cover.'
    s3 = 'Apart from the Himalayan region, this soil also found in the Western and the Eastern Ghats and some parts of the Peninsular India'
    desc = [s1,s2]

    mountain = Soil(crops_grown=['Wheat', 'Maize', 'Barley', 'Apple', 'Pear', 'Peach', 'Plum', 'Grapes', 'Strawberry', 'Tea', 'Coffee'], description=desc)
    data = {'crop': mountain.crops_grown, 'description': desc, 'name':'Mountain Soil'}
    return data

def laterite_soil_data():
    s1 = 'Laterite and lateritic soils submitted to South Maharashtra, the Western Ghats in Kerala and Karnataka, at places on the Eastern Ghats, in some parts of Assam, Tamil Nadu, Karnataka, and in western West Bengal (particularly in Birbhum district). These soils are infertile.'
    desc = [s1]
    laterite = Soil(crops_grown=['Tea','Coffee', 'Coconut', 'Areca nut', 'Rubber'],description=desc)
    data = {'crop': laterite.crops_grown, 'description': desc,'name':'Laterite Soil'}
    return data

def desert_soil_data():

    s1 = 'The desert soil has sand (90 to 95 percent) and clay (5 to 10 percent). In some regions this soil has the high percentage of soluble salts, but lacks in organic matter. The nitrogen content is low, but the phosphate content is as high as in average alluvial soil.'
    s2 = 'The desert soil is found mostly in the arid and semi-arid regions, receiving less than 50 cm of annual rainfall. Such regions mostly found in Rajasthan and the adjoining areas of Haryana and Punjab. The Rann of Kachchh in Gujarat is an extension of this area.'
    desc=[s1,s2]
    desert = Soil(crops_grown=['Wheat', 'Millets', 'Barley', 'Maize', 'Pulses', 'Cotton'], description=desc)
    data = {'crop': desert.crops_grown, 'description': desc, 'name':'Desert Soil'}
    return data





def soil_to_crop(soil_type):
    if soil_type == 'soil_type_alluvial':
        data = alluvial_soil_data()
        crop_list = data['crop']
        return {'soil_type':'Alluvial Soil','crop_list':crop_list}
    elif soil_type =='soil_type_red':
        data = red_soil_data()
        crop_list = data['crop']
        return {'soil_type':'Red Soil','crop_list':crop_list}
    elif soil_type =='soil_type_black':
        data = black_soil_data()
        crop_list = data['crop']
        return {'soil_type':'Black Soil','crop_list':crop_list}
    elif soil_type =='soil_type_mountain':
        data = mountain_soil_data()
        crop_list = data['crop']
        return {'soil_type':'Mountain Soil','crop_list':crop_list}
    elif soil_type =='soil_type_laterite':
        data = laterite_soil_data()
        crop_list = data['crop']
        return {'soil_type':'Laterite Soil','crop_list':crop_list}
    elif soil_type =='soil_type_desert':
        data = desert_soil_data()
        crop_list = data['crop']
        return {'soil_type':'Desert Soil','crop_list':crop_list}

def crop_name_converter(crop_option_list):
    if crop_option_list == 'crop_option_rice':
        return 'Rice'
    if crop_option_list == 'crop_option_wheat':
        return 'Wheat'
    if crop_option_list == 'crop_option_sugarcane':
        return 'Sugarcane'
    if crop_option_list == 'crop_option_groundnut':
        return 'Groundnut'
    if crop_option_list == 'crop_option_apple':
        return 'Apple'
    if crop_option_list == 'crop_option_strawberry':
        return 'Strawberry'
    if crop_option_list == 'crop_option_maize':
        return 'Maize'
    if crop_option_list == 'crop_option_grapes':
        return 'Grapes'
    if crop_option_list == 'crop_option_coffee':
        return 'Coffee'

def soil_name_converter(soil_type_code):
    if soil_type_code == 'soil_type_alluvial':
        return 'Alluvial Soil'
    if soil_type_code == 'soil_type_red':
        return 'Red Soil'
    if soil_type_code == 'soil_type_black':
        return 'Black Soil'
    if soil_type_code == 'soil_type_mountain':
        return 'Mountain Soil'
    if soil_type_code == 'soil_type_laterite':
        return 'Laterite Soil'
    if soil_type_code == 'soil_type_desert':
        return 'Desert Soil'

def crop_to_soil(crop_option_list):

    data_alluvial = alluvial_soil_data()
    data_black = black_soil_data()
    data_red = red_soil_data()
    data_mountain = mountain_soil_data()
    data_laterite = laterite_soil_data()
    data_desert = desert_soil_data()
    soil_compatible =[]
    crop_option = crop_name_converter(crop_option_list)

    if crop_option in data_alluvial['crop']:
        soil_compatible.append('Alluvial')
    if crop_option in data_red['crop']:
        soil_compatible.append('Red')
    if crop_option in data_black['crop']:
        soil_compatible.append('Black')
    if crop_option in data_mountain['crop']:
        soil_compatible.append('Mountain')
    if crop_option in data_laterite['crop']:
        soil_compatible.append('Laterite')
    if crop_option in data_desert['crop']:
        soil_compatible.append('Desert')
    crop_soil_compatibility = {'crop_option_result':crop_option, 'soil_list':soil_compatible}
    return crop_soil_compatibility
