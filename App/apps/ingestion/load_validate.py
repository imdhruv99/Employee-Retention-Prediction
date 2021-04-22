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