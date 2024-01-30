import streamlit as st
import requests

# Function to send messages to Rasa and get responses
def send_message_to_rasa(message):
    url = 'http://localhost:5005/webhooks/rest/webhook'  # URL of the Rasa server
    payload = {"sender": "streamlit_user", "message": message}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return [{"text": "Sorry, I couldn't process that request."}]


# Streamlit UI
def main():
    st.title("FoodleBot: Restaurant Search Assistant (Prague Shisha University development)")
    
    user_input = st.text_input("Type your message here and press enter:")

    if user_input:
        # Send the user message to Rasa
        bot_responses = send_message_to_rasa(user_input)

        # Display bot responses
        for response in bot_responses:
            st.text_area("FoodleShishaBot:", value=response.get("text", ""), height=100, disabled=True)

if __name__ == "__main__":
    main()
