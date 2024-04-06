#Invoice Extractor
import os
import streamlit as st

from PIL import Image # this will help to get info from images
import google.generativeai as genai 

from dotenv import load_dotenv

load_dotenv() # it will load all environment variables from .env

key=os.getenv("GOOGLE_API_KEY")

# Configure genai
genai.configure(api_key=key)


# Function to load Gemni Pro Vision model and get response

# Input is what gemni pro vision is going to do 
def get_gemni_response(input,image,prompt):         # prompt is like my input like image,text etc...
    # loadin gemni model
    model=genai.GenerativeModel("models/gemni-pro-vision") 
    response=model.generate_content([input,image[0],prompt]) #Input will be form of list
    return response.text

# Image setup
def image_setup(uploaded_file):
    """
        This function is going to perform what information is contain in the image
        which we convert them to bytes

    """
    if uploaded_file is not None:

        #read file into bytes
        bytes_data=uploaded_file.getvalue()

        images_parts=[{
            "mime_type":uploaded_file.type, #get the mime type of the uploaded file
            "data":bytes_data
        }]
        return images_parts
    else:
        raise FileNotFoundError("No File uploaded")
    

# Initialize streamlit app

st.set_page_config(page_title="Gemni Pro Vision")

st.header("Gemni Pro Vision Invoice Extractor")

input=st.text_input("Input prompt:",key="input")
uploaded_file=st.file_uploader("Choose an  image..",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    # below 2 line help to show our uploaded image
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded image",use_column_width=True) 

submit=st.button("Tell me about invoice")

# I am going to tell my model to behave like
input_prompt="""
    You are an expert in understanding invoices.you will receive
    input images as invoices and you will have to answer questions
    based on the input images

"""

if submit:
    # Image data fuction to get byts data from the image
    image_data=image_setup(uploaded_file)
    # Calling the model
    response=get_gemni_response(input_prompt,image_data,input)

    st.subheader("The response is:")
    st.write(response)

