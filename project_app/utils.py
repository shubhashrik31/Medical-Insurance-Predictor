import numpy as np
import pandas as pd
import config
import pickle
import json

import warnings
warnings.filterwarnings('ignore')

class MedicalInsurance:
    
    def __init__(self,age,bmi,sex,children,smoker,region):
        
        self.age = age
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.sex = sex
        self.region = region
        
    def load_model(self):
        #self.model = pickle.load(open('linear_model.pkl','rb'))
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)

        
    def load_json(self):
        with open(config.JSON_FILE_PATH, 'r') as f:
            self.project_data = json.load(f) 
        
        #self.project_data = json.load('project_data.json','r')
        
    def predict_charges(self):
        self.load_json()
        self.load_model()
        print(self.project_data)
        column_names = self.project_data['columns']
        new_region = 'region_'+self.region
        region_index = np.where(column_names == new_region)
        test_array = np.zeros(9)
        test_array[0] = self.age
        test_array[1] = self.project_data['sex'][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.project_data['smoker'][self.smoker]
        test_array[region_index] = 1
        
        result = self.model.predict([test_array])
        return result[0]

if __name__ == '__main__':
    obj=MedicalInsurance(49,25.7,'female',2,'no','southeast')
    obj.predict_charges()