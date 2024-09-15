import pickle
import warnings
warnings.filterwarnings('ignore')
import numpy as np
loaded_model = pickle.load(open('rent_prediction_bay_area', 'rb'))
feature_order=['bedrooms',
               'bathrooms',
               'walkability_score',
               'is_renovated',
               'has_washer_dryer',
               'county_alameda',
               'county_contra_costa',
               'county_marin',
               'county_napa',
               'county_san_francisco',
               'county_san_mateo',
               'county_santa_clara',
               'county_solano',
               'county_sonoma']

api_response={'county':'San Francisco','bedrooms':1,'bathrooms':2,'walkability_score':'High','is_renovated':True,'has_washer_dryer':True}

def map_walkability(val):
    if val=='High':
        return 80
    elif val=='Medium':
        return 60
    else:
        return 25

def map_api_response(api_response, feature_order):
    # Initialize a list to hold the mapped values
    result = []

    # Extracting known fields from api_response
    for feature in feature_order:
        if feature in api_response:
            value = api_response[feature]
            if isinstance(value, bool):
                result.append(int(value))  # Convert boolean to int (True -> 1, False -> 0)
            elif feature=='walkability_score':
                result.append(map_walkability(api_response[feature]))
            else:
                result.append(value)
        else:
            # Handle county-specific fields
            if feature.startswith('county_'):
                county_name = feature[len('county_'):]  # Extract the county part
                # Check if the county matches the one in api_response
                if county_name.replace('_', ' ').lower() == api_response['county'].lower():
                    result.append(1)
                else:
                    result.append(0)

    return result


input = np.array(map_api_response(api_response, feature_order)).reshape(1, -1)
#print(input)
print(int(loaded_model.predict(input)[0]))