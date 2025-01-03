import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = st.secrets["OPEN_AI_KEY"]

# Function to generate a response from OpenAI
def get_openai_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=200,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit app
st.title("Simple Chatbot")
st.write("Powered by OpenAI and Streamlit")

# Store chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
with st.container():
    col1, col2 = st.columns([6, 1])  # Adjust column width ratios as needed
    with col1:
        user_input = st.text_area("Type your message:", key="user_input", label_visibility="collapsed")
    with col2:
        send_button = st.button("➡️", key="send_button")

# Handle user input
if send_button and user_input.strip():
    st.session_state.messages.append({"role": "user", "content": user_input.strip()})
    bot_response = get_openai_response(user_input.strip())
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    # Clear input after submission
    st.session_state.user_input = ""

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"**You:** {message['content']}")
    else:
        st.write(f"**Bot:** {message['content']}")
