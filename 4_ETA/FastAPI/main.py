from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from Features import Categories
import numpy as np
import pickle

app = FastAPI()

global params 
params = {
            "day_of_week": Categories().list_other_categories("day_of_week"),
            "month": Categories().list_other_categories("month"),
            "taxi_company": Categories().list_other_categories("taxi_company"),
            "wind_direction": Categories().list_other_categories("wind_direction"),
            "dispatching_base_num": Categories().list_other_categories("dispatching_base_num"),
            "PULocationId": Categories().list_locationid(),
            "DOLocationId" : Categories().list_locationid(),
        }
class paramEnum(str, Enum):
    pul = 'PULocationId'
    dol = 'DOLocationId'
    week = 'day_of_week'
    dbn = 'dispatching_base_num'
    month = 'month'
    taxi = 'taxi_company'
    wd = 'wind_direction'

@app.get("/categorical_parameters")
async def list_parameters():
    # "PUBorough": [],          # get these values from dataset
            # "DOBorough": [],
            # "PUservice_zone": [],
            # "DOservice_zone": [],
    return params

@app.get("/categorical_parameters/{parameter}")
async def get_parameters(parameter: paramEnum):
    return params[parameter]
    
class InputParams(BaseModel):
    taxi_company: str
    trip_miles: float
    wav_request_flag: bool
    wav_match_flag: bool
    dispatching_base_num: str
    PULocationID: int
    DOLocationID: int
    any_tolls: bool
    hour_of_day: int
    day_of_week: str
    month: str
    traffic: int
    feel: float
    humidity: float
    BR: bool
    CLR: bool
    SN: bool
    wind_speed: float
    wind_direction: str


@app.post("/predict")
async def prediction(inputParam: InputParams):
    puloc_info = Categories().get_locationid_info(inputParam.PULocationID)
    doloc_info = Categories().get_locationid_info(inputParam.DOLocationID)

    if puloc_info =='NA' or doloc_info =='NA':
        return "Location ID not in data. Check get(/categorical_parameters/parameters)"

    param_dict = dict(inputParam)
    train_cols = ['taxi_company', 'trip_miles',  'wav_request_flag', 'wav_match_flag', 'dispatching_base_num', 
                'PULocationID', 'PUBorough', 'PUservice_zone', 'DOLocationID', 'DOBorough', 'DOservice_zone', 
                'any_tolls', 'hour_of_day', 'day_of_week', 'month', 'traffic',
                'feel', 'humidity', 'BR', 'CLR', 'SN', 'wind_speed', 'wind_direction']
    train_dict = {}
    for column in train_cols:
        train_dict[column] = param_dict.get(column, None)

    cat_col = ['taxi_company', 'day_of_week', 'dispatching_base_num', 'month', 'wind_direction']
    for column in cat_col:
        value = Categories().get_other_categories_info(column, train_dict[column])
        if value==None:
            return column+" value not in database. Check get(/categorical_parameters/{parameters)"
        train_dict[column] = value
    
    bool_col = ['wav_request_flag', 'wav_match_flag', 'any_tolls', 'BR', 'CLR', 'SN']
    for column in bool_col:
        if train_dict[column]:
            train_dict[column] = 1
        else:
            train_dict[column] = 0

    train_dict['PUBorough'] = int(puloc_info['borough'])
    train_dict['DOBorough'] = int(doloc_info['borough'])
    train_dict['PUservice_zone'] = int(puloc_info['service_zone'])
    train_dict['DOservice_zone'] = int(doloc_info['service_zone'])

    features = np.array(list(train_dict.values()))
    features = features.reshape(1, -1)
    print(features)
    model = pickle.load(open("xgb_model.pkl", 'rb'))
    minute_pred = float(model.predict(features)[0])
    pred = minute_pred*train_dict['trip_miles']

    return pred

    