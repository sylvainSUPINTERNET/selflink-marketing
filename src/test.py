from googleapiclient.discovery import build

youtube = build('youtube', 'v3', developerKey='AIzaSyDEcc93sGb8nfxZ-Wg_Myt-uIbeURuQ47c')

videos_test = youtube.search().list(part='snippet', q='python', type='video').execute()
print(videos_test)