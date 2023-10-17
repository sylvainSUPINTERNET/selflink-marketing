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



# def build_tree_microinfluenceur(sheets_name_list:List[str]):
#     current_path = os.path.dirname(f"{os.path.abspath(__file__)}")
#     all_sheets_df = pd.read_excel(current_path+"/micro_influenceur.xlsx", sheet_name=None)
    
    
#     for (sheet_name, df) in all_sheets_df.items():
        
#         if sheet_name in sheets_name_list:
#             logging.info("sheet_name: %s", sheet_name)
                