import streamlit as st

st.title("AI-Chatbot")
st.write("Hi, I am a chatbot. Type 'bye' to end (just refresh the page to restart).")

if "messages" not in st.session_state:
    st.session_state.messages = []

def get_response(user):
    user = user.lower().strip()

    if user in ["bye", "exit", "quit"]:
        return "Goodbye, take care!"
    elif user in ["hi", "hello"]:
        return "Hello there! How can I help you?"
    elif user in ["how are you"]:
        return "Doing great!"
    elif user in ["whats your name"]:
        return "My name is AI-CHATBOT"
    elif user in ["who created you", "who built you"]:
        return "I am created by some person using Python language"
    elif "bored" in user:
        return "Let's talk then! Tell me something about yourself."
    else:
        return "I can understand this, try again!"

for role, text in st.session_state.messages:
    with st.chat_message(role):
        st.write(text)

user_input = st.chat_input("You:")

if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    response = get_response(user_input)
    st.session_state.messages.append(("assistant", response))
    with st.chat_message("assistant"):
        st.write(response)