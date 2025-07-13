"""
Configuration file for the AI Assistant Chat app.
This file contains default settings and configuration options.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = st.secrets["api_key"]
ASSISTANT_ID = os.getenv("ASSISTANT_ID", "asst_PytLeS8CwhZiswnc11HCsmbO")

# System Prompt for the Assistant
ASSISTANT_SYSTEM_PROMPT = "You are a helpful assistant. Rely solely on the supplied knowledge base. If the answer isn’t there, reply: ‘I’m sorry, that information isn’t in my database. Please re-ask using topics the database covers. Keep every reply directly focused on the question.Present the reply as a numbered or bulleted list.'"

# ASSISTANT_SYSTEM_PROMPT = """
# You are a helpful assistant.

# • Use only the supplied knowledge base—no outside facts or guesses.  
# • If the answer is not in the data, reply exactly:  
#   “I’m sorry, that information isn’t in my database. Please re-ask using topics the database covers.”  
# • Keep every reply short and directly focused on the question (1-2 sentences max).
# """

# App Configuration
APP_TITLE = "AI Assistant Chat"
APP_ICON = "🤖"
PAGE_LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

# Chat Configuration
MAX_MESSAGE_LENGTH = 4000  # Maximum length for user messages
THINKING_TIMEOUT = 60  # Maximum time to wait for assistant response (seconds)
POLLING_INTERVAL = 1  # Time between status checks (seconds)

# UI Configuration
CHAT_INPUT_PLACEHOLDER = "Type your message here..."
INIT_BUTTON_TEXT = "🚀 Initialize Chat"
CLEAR_BUTTON_TEXT = "🗑️ Clear Chat History"
THINKING_MESSAGE = "🤔 Assistant is thinking..."

# Error Messages
ERROR_MESSAGES = {
    "no_api_key": "❌ Please provide your OpenAI API key",
    "no_assistant_id": "❌ Please provide your Assistant ID",
    "connection_failed": "❌ Failed to connect to OpenAI",
    "thread_creation_failed": "❌ Failed to create thread",
    "message_send_failed": "❌ Failed to send message",
    "response_failed": "❌ Assistant failed to respond",
    "timeout": "⏰ Request timed out",
}

# Success Messages
SUCCESS_MESSAGES = {
    "chat_initialized": "✅ Chat initialized successfully!",
    "chat_cleared": "✅ Chat history cleared!",
}

# CSS Styles
CUSTOM_CSS = """
<style>
.error-box {
    background: #f8d7da;
    color: #721c24;
    padding: 0.75rem;
    border-radius: 6px;
    margin: 0.5rem 0;
    border-left: 4px solid #dc3545;
}
.user-message {
    background-color: #2e2e2e; /* Darker background for user messages */
    border-left-color: #007bff; /* Keep a distinct color */
    color: #ffffff; /* White text for contrast */
}
.assistant-message {
    background-color: #1a1a1a; /* Even darker background for assistant messages */
    border-left-color: #28a745; /* Keep a distinct color */
    color: #ffffff; /* White text for contrast */
}
/* Remove default Streamlit padding around main content */
.main > div {
    padding-left: 1rem;
    padding-right: 1rem;
}

/* Ensure chat messages have consistent padding/margins */
.stChatMessage {
    margin-bottom: 0.5rem;
    margin-top: 0.5rem;
}

/* Adjust chat input to avoid covering responses */
.stChatInput {
    margin-top: 2rem; /* Increased margin to push it down */
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
    background-color: #303030; /* Darker background for input bar */
    border-radius: 10px;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.3); /* Subtle shadow for separation */
    border: 1px solid #444444; /* Darker border */
}
.stChatInput input[type="text"] {
    background-color: #262626; /* Input field background */
    color: #ffffff; /* Input text color */
    border: 1px solid #555555; /* Input border */
    border-radius: 8px;
    padding: 10px;
}
.stChatInput input[type="text"]:focus {
    border-color: #008000; /* Green border on focus */
    box-shadow: 0 0 0 0.1rem rgba(0, 128, 0, 0.25); /* Green shadow on focus */
}
/* Hide Streamlit's default red border on invalid input */
.st-emotion-cache-1c05n0q { /* This class targets the input container when invalid */
    border-color: #555555 !important; /* Override red border with a neutral one */
}


</style>
""" 
