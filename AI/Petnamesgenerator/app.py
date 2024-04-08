import helper as hp
import streamlit as st

st.title("Pet name generator")

animal_type=st.sidebar.selectbox("what is you pet ?",("dog","cat","parret","cow","goat"))

if animal_type=="cat":
    pet_color=st.sidebar.text_area("what color of your cat:",max_chars=10)

if animal_type=="dog":
    pet_color=st.sidebar.text_area("what color of your dog:",max_chars=10)

if animal_type=="parret":
    pet_color=st.sidebar.text_area("what color of your parret:",max_chars=10)

if animal_type=="cow":
    pet_color=st.sidebar.text_area("what color of your cow:",max_chars=10)

if animal_type=="goat":
    pet_color=st.sidebar.text_area("what color of your goat:",max_chars=10)

if st.button("Suggest names"):
    response=hp.generate_pet_name(animal_type,pet_color)
    st.text(response["petname"])