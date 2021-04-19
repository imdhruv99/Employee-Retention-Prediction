from datetime import datetime

import random

class Config:

    def __init__(self):
        self.training_data_path = 'data/training/training_data'
        self.training_database = 'training'
        self.prediction_data_path = 'data/prediction/prediction_data'
        self.prediction_database = 'prediction'
    
    def  get_run_id(self):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H%M%S")
        return str(self.date)+"_"+str(self.current_time)+"_"+str(random.randint(1000000000, 9999999999))
        