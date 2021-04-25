import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from apps.core.logger import Logger


class Preprocessor:


    def __init__(self, run_id, data_path, mode):
        self.run_id = run_id
        self.data_path = data_path
        self.logger = Logger(self.run_id, 'Preprocessor', mode)

    
    def get_data(self):

        try:
            # reading the data file
            self.logger.info("Start of Reading Dataset...")
            self.data = pd.read_csv(self.data_path+'_validation/InputFile.csv')
            self.logger.info("End of Reading Dataset...")
        
        except Exception as e:

            self.logger.exception('Exception raised while reading dataset: %s'+str(e))
            raise Exception()
    

    def drop_column(self, data, columns):

        self.data = data
        self.columns = columns
        
        try:

            self.logger.info("Start of Droping columns...")
            self.useful_data = self.data.drop(labels = self.columns, axis=1) # drop the label specified in the columns
            self.logger.info("End of Droping columns...")

        except Exception as e:

            self.logger.exception('Exception raised while Droping Columns:'+str(e))
            raise Exception()
    
    def is_null_present(self, data):

        self.null_present = data

        try:

            self.logger.info("Start of finding missing values...")

            self.null_counts = data.isna().sum() # check for the count of null values per column

            for i in self.null_counts:

                if i > 0:
                    self.null_present = True
                    break
            
            if (self.null_present): #write the logs to see which columns have null values
                dataframe_with_null = pd.DataFrame()
                dataframe_with_null['columns'] = data.columns
                dataframe_with_null['missing values count'] = np.asarray(data.isna().sum())
                dataframe_with_null.to_csv(self.data_path+'_validation/'+'null_values.csv') # storing the null column information to file
            self.logger.info('End of finding missing values...')
            return self.null_present
            
        except Exception as e:
            self.logger.exception('Exception raised while finding missing values:'+str(e))
            raise Exception()