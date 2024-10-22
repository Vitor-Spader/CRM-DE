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
    
    def insert(self, table:str, data:pd.DataFrame):
        self.__write(table, data, False)

    def upsert(self, table:str, data:pd.DataFrame, is_upsert:bool):
        self.__write(table, data, True)

    def delete(self, table:str, ids:list[str]):

        self.CONNECTION.rollback()

        sql = f"DELETE FROM {table} WHERE id in ({ids.join(',')})"

        self.CONNECTION.cursor().execute(sql)
        self.CONNECTION.commit()

        
    def __write(self, table:str, data:pd.DataFrame, is_upsert:bool):

        self.CONNECTION.rollback()

        columns = [col for col in data.columns if col != 'id']

        if is_upsert:
            update_set_clause = ", ".join([f"{col} = excluded.{col}" for col in columns])
        

        for _, row in data.iterrows():
            
            sql = f"INSERT INTO {table} (id, {', '.join(columns)}) VALUES (?, {', '.join(['?'] * len(columns))})"
            
            if is_upsert:
                sql = sql + f" ON CONFLICT(id) DO UPDATE SET {update_set_clause};"

            values = [row['id']] + [row[col] for col in columns]
            self.CONNECTION.cursor().execute(sql, values)
            self.CONNECTION.commit()