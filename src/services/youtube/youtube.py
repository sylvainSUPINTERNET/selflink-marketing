from typing import List
import pandas as pd
import os
from logger.logger import logging

def get_categories() -> List[str]:
    current_path = os.path.dirname(f"{os.path.abspath(__file__)}")
    all_sheets_df = pd.read_excel(current_path+"/micro_influenceur.xlsx", sheet_name=None)
    return list(all_sheets_df.keys())

def get_subcategory() -> List[str]:
    current_path = os.path.dirname(f"{os.path.abspath(__file__)}")
    all_sheets_df = pd.read_excel(current_path+"/micro_influenceur.xlsx", sheet_name=None)
    
    m = set()
    for (_, df) in all_sheets_df.items():
        m.update(df["sub_category"].unique())
    return list(m)

def get_influenceur() -> List[str]:
    current_path = os.path.dirname(f"{os.path.abspath(__file__)}")
    all_sheets_df = pd.read_excel(current_path+"/micro_influenceur.xlsx", sheet_name=None)
    
    m = set()
    for (_, df) in all_sheets_df.items():
        m.update(df["channel_name"].unique())
    return list(m)


def get_influenceur_all_categories() -> dict:
    resp = dict()
    current_path = os.path.dirname(f"{os.path.abspath(__file__)}")
    

    for category in pd.read_excel(current_path+"/micro_influenceur.xlsx", sheet_name=None).keys():
        df = pd.read_excel(current_path+"/micro_influenceur.xlsx", sheet_name=category)
        resp[category] = list(df["channel_name"].unique())
        
    return resp
