from typing import List
from repositories.YoutubeInfluenceur import YoutubeInfluenceur
from dotenv import load_dotenv

from services.youtube.youtube import get_categories, get_influenceur, get_subcategory
load_dotenv()


def main():
    cat_list = get_categories()
    subcat_list = get_subcategory()
    influenceur_list = get_influenceur()
    
    youtube_influenceur = YoutubeInfluenceur()
    
    youtube_influenceur.build_tree_add_node_category()
    youtube_influenceur.build_tree_add_node_subcategory()
    
    youtube_influenceur.insert_category(cat_list)
    youtube_influenceur.insert_subcategory(subcat_list)
    
    for influenceur in influenceur_list:
        youtube_influenceur.insert_influenceur(influenceur)
    
    youtube_influenceur.close()

if __name__ == "__main__":
    main()