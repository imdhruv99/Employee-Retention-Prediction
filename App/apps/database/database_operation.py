import sqlite3
import csv
from os import listdir
import shutil
import os

from apps.core.logger import Logger


class DatabaseOperation:

    def __init__(self, run_id, data_path, mode):

        self.run_id = run_id
        self.data_path = data_path
        self.logger = Logger(self.run_id, 'DatabaseOperation', mode)
    
    def database_connection(self, database_name):
        
        try:
            conn = sqlite3.connect('apps/database/'+ database_name +'.db')
            self.logger.info("Opened %s database successfully"% database_name)
        except ConnectionError:
            self.logger.info("Error while connecting to database: %s" %ConnectionError)
        return conn
    
    def create_table(self, database_name, table_name, column_names):

        try:
            self.logger.info("Start of creation Table...")
            conn = self.database_connection(database_name)
        
            if (database_name == 'prediction'):
                conn.execute("DROP TABLE IF EXISTS"+table_name+"';")

            c = conn.cursor()
            c.execute("SELECT count(name) FROM sqlite_master WHERE type = 'table' AND name= '"+table_name+"'")
            
            if c.fetchone()[0] == 1:
                conn.close()
                self.logger.info("Tables created successfully")
                self.logger.info("closed %s database successfully"%database_name)
            else:
                for key in column_names.keys():
                    type = column_names[key]

                    try:
                        conn.execute("ALTER TABLE "+table_name+" ADD COLUMN {column_name} {dataType}".format(column_name=key,dataType=type))
                        self.logger.info("ALTER TABLE "+table_name+" ADD COLUMN")
                    except:
                        conn.execute("CREATE TABLE  "+table_name+" ({column_name} {dataType})".format(column_name=key, dataType=type))
                        self.logger.info("CREATE TABLE "+table_name+" column_name")
                conn.close()
            self.logger.info('End of creating Table...')
        
        except Exception as e:

            self.logger.exception("Exception raised while creating Table: %s"%e)
            raise e