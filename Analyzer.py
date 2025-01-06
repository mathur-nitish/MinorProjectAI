import requests
import json
from collections import Counter

starting = ""
destination = ""

import pandas as pd
import joblib
from sklearn.preprocessing import OneHotEncoder, StandardScaler
model = joblib.load('random_forest_model.pkl')

def predict_speed(data):
    # Perform the same preprocessing as during training
    # One-hot encoding
    ohe = OneHotEncoder(sparse_output=False)
    temp_encoder = ohe.fit_transform(data[['Service Provider']])
    location_encoder = ohe.fit_transform(data[['LSA']])
    tech_encoder = ohe.fit_transform(data[['Technology']])
    test_type_encoder = ohe.fit_transform(data[['Test_type']])

    # Concatenate encoded data
    encoded_df = pd.concat([
        pd.DataFrame(temp_encoder, columns=ohe.get_feature_names_out(ohe.feature_names_in_)),
        pd.DataFrame(location_encoder, columns=ohe.get_feature_names_out(ohe.feature_names_in_)),
        pd.DataFrame(tech_encoder, columns=ohe.get_feature_names_out(ohe.feature_names_in_)),
        pd.DataFrame(test_type_encoder, columns=ohe.get_feature_names_out(ohe.feature_names_in_))
    ], axis=1)

    data = pd.concat([data.drop(columns=['Service Provider', 'LSA', 'Technology', 'Test_type']), encoded_df], axis=1)
    data.fillna(0, inplace=True)
    scaler = StandardScaler()
    data = scaler.fit_transform(data)
    prediction = model.predict(data)

    return prediction



def analyze_payments(start_location, end_location):
    # Call the API to get nearby restaurants
    url = "http://127.0.0.1:8000/nearby-restaurants"
    params = {
        "start_location": start_location,
        "end_location": end_location,
        "num_restaurants": 15
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        nearby_restaurants = response.json()
        payment_counter = Counter()

        for restaurant in nearby_restaurants:
            if restaurant.get('paymentOptions'):
                for option in restaurant['paymentOptions']:
                    if option:
                        payment_counter[option] += 1

        total_digital = payment_counter.get('Digital-Payment', 0)
        total_cash = payment_counter.get('Cash', 0)


        if total_digital > total_cash:
            recommendation = "Digital Payments"
        elif total_cash > total_digital:
            recommendation = "Cash"
        else:
            recommendation = "Both"

        return recommendation
    else:
        return f"Failed to retrieve data: {response.status_code}"


# Example usage
