import requests
import json
import requests
import datetime 
inventory = {}

def api_grab (barcode):
    product_info = requests.get("https://world.openfoodfacts.org/api/v0/product/"+barcode+".json")
    
    response_dict = json.loads(product_info.text)

    for key, value in response_dict.items():
        if key == "product":
            for key1, value1 in value.items():
                if key1 == "serving_quantity":
                    serving_amount = value1
                elif key1 == "quantity":
                    total_amount = value1

    return [serving_amount,total_amount]



def calculator(total_amount, serving_size, spw):
    max_servings = total_amount/serving_size
    days = max_servings/(spw/7)
    current_servings = max_servings
    today = datetime.date.today()
    return [max_servings, current_servings, days, today, spw]

def manual_add(name, total_amount, serving_size, spw):
    max_servings = total_amount/serving_size
    days = max_servings/(spw/7)
    current_servings = max_servings
    today = datetime.date.today()
    inventory[name] = [max_servings, current_servings, days, today, spw]

def update(name, num_bought):
    inventory[name][1] = inventory[name][1] + (inventory[name][0]*num_bought)

def update_time(name):
    days_elapsed = inventory[name][3] - datatime.date.today()
    inventory[name][1] = inventory[name][0] - (inventory[name][4]/7)*days_elapsed


    

