# from googleapiclient.discovery import build

# youtube = build('youtube', 'v3', developerKey='AIzaSyDEcc93sGb8nfxZ-Wg_Myt-uIbeURuQ47c')

# videos_test = youtube.search().list(part='snippet', q='python', type='video').execute()
# print(videos_test)

from dotenv import load_dotenv
load_dotenv()

from repositories.YoutubeInfluenceur import YoutubeInfluenceur


def main():
    m = YoutubeInfluenceur()
    m.insert_category(["LIFESTYLE", "FORMATION", "SPIRITUAL"])
    m.insert_subcategory(["sub1", "sub2", "sub3"])
    # m.build_tree_add_node_category( )
    # m.insert_influenceur("SYLVAIN")
    # m.insert_category("LIFESTYLE")
    # m.insert_category("XD")
    #m.close()

    
if __name__ == "__main__":
    main()