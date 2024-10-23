from ingestion.controller.IDatabase import IDatabase
from pydantic import BaseModel
import pandas as pd

class IngestionController:

    def __init__(self, data_object:list[BaseModel], is_upsert:bool):
        self.dataframe = pd.DataFrame([data.__dict__ for data in data_object]) 
        self.is_upsert = is_upsert

    def set_filters(self):
        pass
    
    def set_formulas(self):
        pass

    def write(self, output_connection:IDatabase):
        
        if self.is_upsert:
            output_connection.upsert(self.dataframe)
        else:
            output_connection.upsert(self.dataframe)