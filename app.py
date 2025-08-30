from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os

##############################
# SETTINGS
##############################

# Load the Google API Key from Streamlit's secrets
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
REMOTE_MODEL_NAME = "gemini-1.5-flash"

# Initialize the Gemini Model
try:
    llm = ChatGoogleGenerativeAI(
        model=REMOTE_MODEL_NAME,
        google_api_key=GOOGLE_API_KEY,
        convert_system_message_to_human=True
    )
except Exception as e:
    st.error(f"Error initializing the language model: {e}")
    st.stop()


##############################
# GUI
##############################

st.title("Cloud-Powered Chatbot")

# Initialize Chat Message Memory
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display Chat Message History from Memory
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Collect User Prompt
prompt = st.chat_input("Type your message...")

# If New User Prompt was Submitted
if prompt:
    # Add the New User Prompt to Memory
    st.session_state["messages"].append(
        {"role": "user", "content": prompt}
    )
    # Display the New User Prompt
    with st.chat_message("user"):
        st.write(prompt)

    # Generate Model Response
    try:
        response = llm.invoke(prompt)
        response_content = response.content
    except Exception as e:
        response_content = f"Sorry, I encountered an error: {e}"

    # Add the New Model Response to Memory
    st.session_state["messages"].append(
        {"role": "assistant", "content": response_content}
    )
    # Display the New Model Response
    with st.chat_message("assistant"):
        st.write(response_content)
