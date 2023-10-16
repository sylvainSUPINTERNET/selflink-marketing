from typing import List
from services.youtube.youtube import build_tree_microinfluenceur
from dotenv import load_dotenv
load_dotenv()

THEMES:List[str] = ["lifestyle", "formation", "spiritual"]

def main():
    build_tree_microinfluenceur(sheets_name_list=THEMES)

if __name__ == "__main__":
    main()