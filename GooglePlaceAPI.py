# uvicorn GooglePlaceAPI:googlePlaceAPI

import fastapi
import json
import random

class Places:
    def __init__(
            self,
            name,
            delivery,
            goodForChildrem,
            paymentOptions,
            parkingOptions
            ):
        
        self.diplay_Name = name
        self.deliveryOptions = delivery
        self.forChildren = goodForChildrem
        self.paymentOptions = paymentOptions
        self.parkingAvailable = parkingOptions

def generate_nearby_restaurants(num_restaurants, start_location, end_location):
    restaurants = []
    for _ in range(num_restaurants):
        # Synthetic data generation
        name = f"Restaurant {_ + 1}"
    
        deliveryOptions = random.choices(['Take-away', 'Dine-in', None], k=random.randint(1, 2))
        goodForChildren = random.choice([True, False, None])
        paymentOptions = random.choices(['Digital-Payment', 'Cash', 'Card', None], k=random.randint(1, 2))
        parkingAvailable = random.choice([True, False, None])
        
        # Randomly generate a location between start and end locations
        # location = round(random.uniform(start_location, end_location), 2)
        
        # Create restaurant instance
        restaurant = Places(name, deliveryOptions, goodForChildren, paymentOptions, parkingAvailable)
        restaurants.append(restaurant)
    
    return restaurants

googlePlaceAPI = fastapi.FastAPI()


@googlePlaceAPI.get("/nearby-restaurants")
def get_nearby_restaurants(start_location:str, end_location:str, num_restaurants: int):

    nearby_restaurants = generate_nearby_restaurants(num_restaurants, start_location, end_location)
    
    response = [restaurant.__dict__ for restaurant in nearby_restaurants]
    return response