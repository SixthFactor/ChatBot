import openai
import streamlit as st
from openai import OpenAI
import time

OPENAI_API_KEY = st.secrets["api_key"]
client = OpenAI(api_key=OPENAI_API_KEY)
thread = client.beta.threads.create()

# Set the assistant ID and initialize the OpenAI client with your API key
assistant_id = "asst_PytLeS8CwhZiswnc11HCsmbO"        #replace with your own assistant

def ensure_single_thread_id():
    if "thread_id" not in st.session_state:
        thread = client.beta.threads.create()
        st.session_state.thread_id = thread.id
    return st.session_state.thread_id

def stream_generator(prompt, thread_id):
    print(f'first time thread in the function {thread_id}')
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=prompt
    )

    with st.spinner("Wait... Generating response..."):  # Spinner starts before the stream

        stream = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
            stream=True
        )

        # Loop through events in the stream
        for event in stream:
            if event.data.object == "thread.message.delta":
                for content in event.data.delta.content:
                    print(content)
                    if content.type == 'text':
                        yield content.text.value + ""  # Once we yield, the spinner stops
                        time.sleep(0.02)
            else:
                pass

# Configure Streamlit page settings
# st.set_page_config(page_icon=":robot:")

st.title("EIPM Customer Satisfaction Insights")
# st.caption("Welcome to SixthFactor. Speak Directly to Market Intelligence.🌱")

st.session_state.start_chat = True

# Initialize session state variables with default values
if 'start_chat' not in st.session_state:
    st.session_state['start_chat'] = False
    
# Main chat interface
if st.session_state.start_chat:
    if "messages" not in st.session_state:
        st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask question to Steve..")
if prompt:
    # # Ensure thread ID for conversation continuity (assuming this is a function you've defined)
    thread_id = ensure_single_thread_id()
    with st.chat_message("user"):
        st.markdown(prompt)
    # # Display user's message
    st.session_state.messages.append({"role": "user", "content": prompt})
      # Generate and display response from the assistant
    with st.chat_message("assistant"):
        response = st.write_stream(stream_generator(prompt,thread_id))
    st.session_state.messages.append({"role": "assistant", "content": response})




