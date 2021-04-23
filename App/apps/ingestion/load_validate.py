import json
from os import listdir
import shutil
import pandas as pd
from datetime import datetime
import os
from app.database.database_operation import DatabaseOperation
from apps.core.logger import Logger


class LoadValidate:

    def __init__(self, run_id, data_path, mode):
        self.run_id = run_id
        self.data_path = data_path
        self.logger = Logger(self.run_id, 'LoadValidate', mode)
        self.dbOperation = DatabaseOperation(self.run_id, self.data_path, mode)

    
    def values_from_schema(self, schema_file):

        try:
            self.logger.info("Start of Reading values from Schema...")
            with open('apps/database/'+schema_file+'.json', 'r') as f:
                dic = json.load(f)
                f.close()
            
            column_names = dic['ColName']
            number_of_columns = dic['NumberofColumns']
            self.logger.info("End of Reading values from Schema...")
        
        except ValueError:
            self.logger.exception('ValueError raised while Reading values From Schema')
            raise ValueError
        except KeyError:
            self.logger.exception('KeyError raised while Reading values From Schema')
            raise KeyError
        except Exception as e:
            self.logger.exception('Exception raised while Reading values From Schema: %s' % e)
            raise e
        return column_names, number_of_columns
    
    def validate_column_length(self, number_of_columns):

        try:

            self.logger.info("Start of validating column length...")
            for file in listdir(self.data_path):
                csv = pd.read_csv(self.data_path+'/'+file)
                if csv.shape[1] == number_of_columns:
                    pass
                else:
                    shutil.move(self.data_path + '/' + file, self.data_path + '_rejects')
                    self.logger.info("Invalid columns length :: %s"% file)
            
            self.logger.info("End of validating columns length...")

        except OSError:
            self.logger.exception('OSError raised while Validating Column Length')
            raise OSError

        except Exception as e:
            self.logger.exception('Exception raised while Validating Column Length: %s' % e)
            raise e
    
    
    def validate_missing_values(self):

        try:

            self.logger.info("Start of validating missing values...")

            for file in listdir(self.data_path):

                csv = pd.read_csv(self.data_path + '/' + file)

                count = 0

                for columns in csv:

                    if (len(csv[columns]) - csv[columns].count()) == len(csv[columns]):

                        count += 1

                        shutil.move(self.data_path+'/'+file, self.data_path+'_rejects')
                        self.logger.info("All missing values in columns :: %s"%file)
                        break
            
            self.logger.info("End of validating missing values...")
        
        except OSError:
            self.logger.exception('OSError raised while Validating Missing Values')
            raise OSError
        
        except Exception as e:
            self.logger.exception('Exception raised while Validating Missing Values: %s' % e)
            raise e

    def replacing_missing_values(self):

        try:

            self.logger.info("Start of replacing missing values...")

            only_files = [f for f in listdir(self.data_path)]

            for file in only_files:

                csv = pd.read_csv(self.data_path + '/' + file)
                csv.fillna('NULL', inplace=True)
                csv.to_csv(self.data_path+'/'+file, index=None, header=True)
                self.logger.info('%s: File Transformed successfully!!'% file)

            self.logger.info('End of Replacing Missing Values with Null...')
        
        except Exception as e:
            self.logger.exception('Exception raised while Replacing Missing Values with NULL: %s' % e)