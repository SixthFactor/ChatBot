

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai



# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = "AIzaSyC5jVGT9OHx4soEsliU60ByZsieobJPRms"  # Replace this with your real API key

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


# Display the chatbot's title on the page
st.title("🤖 Gemini Pro - ChatBot")

# Predefined prompt for the first message
predefined_prompt = "As a 20-year expert in the fitness field, "

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    # Check if it's the first user's message in the session
    if "first_message_sent" not in st.session_state:
        # Prepend the predefined prompt to the user's first message
        user_prompt_with_context = predefined_prompt + user_prompt
        # Mark the first message as sent in the session state
        st.session_state.first_message_sent = True
    else:
        # For subsequent messages, just use the user's input
        user_prompt_with_context = user_prompt

    # Add user's original message to chat and display it (without the predefined_prompt for clarity)
    st.chat_message("user").markdown(user_prompt)

    # Send the possibly modified user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt_with_context)
