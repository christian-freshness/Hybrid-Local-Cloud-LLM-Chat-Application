from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st
import os

##############################
# SETTINGS
##############################

st.title("Cloud-Powered Chatbot (With Memory)")

# Load the Google API Key from Streamlit's secrets
try:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
except (FileNotFoundError, KeyError):
    st.error("Google API Key not found. Please add it to your Streamlit secrets.")
    st.stop()

REMOTE_MODEL_NAME = "gemini-2.5-flash"

# Initialize the Gemini Model
try:
    llm = ChatGoogleGenerativeAI(
        model=REMOTE_MODEL_NAME,
        google_api_key=GOOGLE_API_KEY
    )
except Exception as e:
    st.error(f"Error initializing the language model: {e}")
    st.stop()


##############################
# GUI
##############################

# Initialize Chat Message Memory in session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display Chat Message History from Memory
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Collect User Prompt
prompt = st.chat_input("Type your message...")

# If a new user prompt was submitted
if prompt:
    # Add the new user prompt to memory and display it
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # --- MEMORY LOGIC ---
    # Convert the session state messages to a format LangChain understands
    chat_history = []
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            chat_history.append(HumanMessage(content=msg["content"]))
        else: # role == "assistant"
            chat_history.append(AIMessage(content=msg["content"]))
    # --- END MEMORY LOGIC ---


    # Generate Model Response using the full chat history
    try:
        response = llm.invoke(chat_history)
        response_content = response.content
    except Exception as e:
        response_content = f"Sorry, I encountered an error: {e}"

    # Add the new model response to memory and display it
    st.session_state["messages"].append({"role": "assistant", "content": response_content})
    with st.chat_message("assistant"):
        st.write(response_content)