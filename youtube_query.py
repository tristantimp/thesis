from googleapiclient.discovery import build
import pandas as pd
import os

#get the API key from the Google Developer Console
API_KEY = os.environ.get("YOUTUBE_API_KEY")
VIDEO_ID = {"biden2021": "UlbyOeMCL0g", "trump2017": "a-mfhjaPvsM", "obama2013":"RvH01Z6ic0M"}

def get_comments(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get comments for the video
    comments = []
    next_page_token = None
    while True:
        response = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            pageToken=next_page_token,
            maxResults=1000
        ).execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append([comment['authorDisplayName'], comment['textOriginal'], comment['publishedAt'],comment['likeCount'], False])
            # Fetch replies to comments
            reply_response = youtube.comments().list(
                part='snippet',
                parentId=item['id'],
                maxResults=100
            ).execute()
            for reply in reply_response['items']:
                comments.append([reply['snippet']['authorDisplayName'], reply['snippet']['textOriginal'], reply['snippet']['publishedAt'], reply['snippet']['likeCount'], True])
        #move to the next page
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return comments

# run this script with a different video_id to get comments for different videos
comments_data = get_comments(API_KEY, VIDEO_ID['obama2013'])

df = pd.DataFrame(comments_data, columns=['Author', 'Comment', 'PublishedAt', 'Likes', 'IsReply'])

df.to_csv('obama2013.csv', index=False)
print("Comments saved to csv")
