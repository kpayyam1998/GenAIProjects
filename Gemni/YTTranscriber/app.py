import os
import google.generativeai as genai
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
load_dotenv()

key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=key)

prompt="""
        You are  youtube summarizer.you will be taking the transcript text and summarizing the entire video and 
        providing the importent summary in point with in 250 words.please  provide the summay of the text given here:   

        """

# getting transcript data from yt video
def extract_transcript_details(youtube_video_url):

    try:
        video_id=youtube_video_url.split("=")[1] # here i will have the only id 

        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript=""

        for i in transcript_text:
            transcript+=" " +i["text"]
        
        return transcript
    except Exception as e:
        raise e

#getting the summary based on the prompt from google gemni pro
def generate_gemini_content(trancript_text,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+trancript_text)

    return response.text

st.title("Youtube video to detailed transcripter")
youtube_link=st.text_input("Enter the youtube link:")

if youtube_link:
    video_id=youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)

if st.button("Explain"):
    transcipt_text=extract_transcript_details(youtube_link)
    if transcipt_text:
        summary=generate_gemini_content(transcipt_text,prompt)
        st.markdown("** Detailed Notes **")
        st.write(summary)


# We can implement more once we get detailed information then we have to store it  info to any one of the DB then we can perform QA operation