import streamlit as st
from gtts import gTTS
import os

# Function to convert text to speech
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    # Use appropriate command based on OS
    os.system("start output.mp3")  # For Windows
    # For Mac, use: os.system("afplay output.mp3")
    # For Linux, use: os.system("mpg321 output.mp3")

# Streamlit app layout
st.title("Text to Speech Chatbot")
st.write("Enter text below and select language for conversion.")

# Text input from user
text_input = st.text_area("Enter your text:", height=150)

# Language selection
language_option = st.selectbox("Select Language", ("English", "Urdu"))

# Convert language option to code
language_code = 'en' if language_option == "English" else 'ur'

# Button to convert text to speech
if st.button("Convert to Speech"):
    if text_input:
        text_to_speech(text_input, language=language_code)
        st.success("Conversion successful! Playing audio.")
    else:
        st.error("Please enter some text to convert.")
