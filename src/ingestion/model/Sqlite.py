from IDatabase import IDatabase
import sqlite3
import traceback
import sys
import pandas as pd
from typing import List

class SQLite(IDatabase):
    CONNECTION = None
    CURSOR = None

    def __init__(self, database:str):
        self.database = database
        SQLite.CONNECTION = sqlite3.connect(database=self.database)
    
    def upsert(self, table:str, data:pd.DataFrame)->bool:
        sql = f"INSERT INTO {table} VALUES('"
        
        columns = [column for column in data]
        
        df = sql + data[columns].agg("','".join, axis=1) + "')"
        
        cursor = self.CONNECTION.cursor()
        for insert in df:
            cursor.execute(insert)

    def delete(ids:list[str])->bool:
        pass

    def append(self, table:str, data:pd.DataFrame)->bool:
        sql = f"INSERT INTO {table} VALUES('"
        
        columns = [column for column in data]
        
        df = sql + data[columns].agg("','".join, axis=1) + "')"
        
        cursor = self.CONNECTION.cursor()
        for insert in df:
            cursor.execute(insert)

    def write(self, table:str, data:any):
        print([x for x in data])
        try:
            if isinstance(data, list):
                self._write_list(data, SQLite.CONNECTION.cursor(), table)
            elif isinstance(data, pd.DataFrame):
                self._write_df(data, table)
            SQLite.CONNECTION.commit()
        except Exception as e:
            raise e

    def _write_df(self, data:pd.DataFrame, table:str):
        sql = f"INSERT INTO {table} VALUES('"

        columns = [column for column in data]
        
        df = sql + data[columns].agg("','".join, axis=1) + "')"
        
        cursor = self.CONNECTION.cursor()
        for insert in df:
            cursor.execute(insert)

    def _write_list(data:list, cursor:sqlite3.Connection, table:str):
        for item in data:
            sql = f"INSERT INTO {table} VALUES((select ifnull(max(idBidding),0)+1 from Bidding),'{"','".join(item)}')"
            print(sql)
            try:
                print(cursor.execute(sql))
                SQLite.CONNECTION.commit()
            except sqlite3.Error as er:
                print('SQLite error: %s' % (' '.join(er.args)))
                print("Exception class is: ", er.__class__)
                print('SQLite traceback: ')
                exc_type, exc_value, exc_tb = sys.exc_info()
                print(traceback.format_exception(exc_type, exc_value, exc_tb))
            except Exception as e:
                raise e
        return
    
    def search(self, _query:str) -> any:
        return SQLite.CONNECTION.execute(_query).fetchall() 
    
    def get_table_columns(self, table:str) -> List[str]:
        cursor = self.CONNECTION.cursor()
        cursor.execute(f'select * from {table} limit 1')
        return [i[0] for i in cursor.description]