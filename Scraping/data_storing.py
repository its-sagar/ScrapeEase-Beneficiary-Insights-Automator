import pandas as pd
from constants import page_list

class DataStoring:
    def show_data(self):
        df = pd.DataFrame(page_list,columns=["NAME", "GENDER", "STATE", "DISTRICT", "SUB DISTRICT", "BLOCK", "VILLAGE"])
        print(df)
