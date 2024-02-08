import pandas as pd
import json

class Categories:
    def __init__(self) -> None:
        self.df = pd.read_csv("locations.csv")
        self.cat_dict = {}
        with open("other_categories.json", "r") as f: 
            self.cat_dict = json.load(f)

    def list_locationid(self):
        location_dict = {x['LocationID']:x['Location'] for i, x in self.df.iterrows()}
        return location_dict
    
    def get_locationid_info(self, locationid):
        location_df =  self.df[self.df['LocationID']==locationid]
        if len(location_df)==0:
            return 'NA'
        location_dict = {
            "borough" :  location_df['Borough'].iloc[0],
            "service_zone" : location_df['service_zone'].iloc[0]
        }
        return location_dict

    def list_other_categories(self, category:str):
        return self.cat_dict[category]
    
    def get_other_categories_info(self, category:str, parm: str):
        parm = parm.capitalize()
        return self.cat_dict[category].get(parm, None)
