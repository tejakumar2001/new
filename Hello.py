import streamlit as st

def chatbot_response(input_text):
    # Define some simple rules or patterns for generating responses
    if "hello" in input_text.lower():
        return "Hi there! How can I help you?"
    elif "how are you" in input_text.lower():
        return "I'm doing well, thank you for asking!"
    elif "bye" in input_text.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand. Can you please rephrase your question?"

def main():
    st.title("💬 Simple Chatbot")

    st.write("Ask me anything!")

    input_text = st.text_input("You")

    if st.button("Send"):
        if input_text:
            response = chatbot_response(input_text)
            st.write("Chatbot:", response)
        else:
            st.write("You:", input_text)
            st.write("Chatbot:", "Please enter a question or message.")

if __name__ == "__main__":
    main()

