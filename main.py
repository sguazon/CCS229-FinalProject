import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=os.getenv("API_KEY"))


if 'chat_session' not in st.session_state:
  model = genai.GenerativeModel('gemini-1.5-pro')
  st.session_state.chat_session = model.start_chat()
  st.session_state.chat_history = []


def handle_chat(question):
  try:
    response = st.session_state.chat_session.send_message(question)
    st.session_state.chat_history.append({"type": "Question", "content": question})
    st.session_state.chat_history.append({"type": "Response", "content": response.text})
    return response
  except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    return None


def classify_feeling(text):
  """
  Classifies the sentiment of the user's text using Gemini's response 
  (note: Gemini might not be specifically trained for sentiment analysis).
  """
  # Send the text to Gemini for analysis, prompting for feeling
  prompt = f"Based on the following text, what is the overall tone or emotion? Is it positive (happy, joyful), negative (sad, angry), or something else?: {text}?"
  response = handle_chat(prompt)

  if response:
    feeling = None
    if "happy" in response.text.lower():
      feeling = "positive"
    elif "sad" in response.text.lower() or "angry" in response.text.lower():
      feeling = "negative"
    else:
      feeling = "neutral"  # If no clear indicator found

    return feeling
  else:
    return None  # Handle potential errors


def main():
  # Feeling Classification Title and Explanation
  st.set_page_config(page_title="Feeling Classification with Gemini")
  st.title("Feeling Classification")
  st.subheader('by Shina Guazon, BSCS 3B AI')
  st.write("This application helps you understand the overall sentiment of your text sing Gemini. ")
  st.write("Tell us what's on your mind, and we'll use Gemini and sentiment analysis to classify your feeling as positive, negative, or neutral.")
  st.write("**Note:** While Gemini is a powerful language model, it may not be specifically trained for sentiment analysis. This means the results might not be **100% accurate**. However, it can still provide a good starting point for understanding the emotional tone of your text.")

  # Feeling Classification UI
  text_input = st.text_area("Tell me how you're feeling:", height=100)

  if st.button("Analyze My Feeling"):
    if text_input:
      feeling = classify_feeling(text_input)
      if feeling:
        st.write(f"It sounds like you're feeling {feeling.title()} today (based on Gemini's analysis).")
      else:
        st.warning("There was an error analyzing your feeling. Please try again.")
    else:
      st.warning("Please enter some text to analyze your feeling.")

  # Conversation History 
  if 'chat_history' in st.session_state:
    st.subheader("Conversation History:")
    for entry in st.session_state.chat_history:
      if entry['type'] == "Question":
        st.markdown(f"*You asked:* {entry['content']}")
      elif entry['type'] == "Response":
        st.markdown(f"*Gemini replied:* {entry['content']}")

  # Reset Conversation Button
  if st.button("Reset Conversation"):
    model = genai.GenerativeModel('gemini-1.5-pro')
    st.session_state.chat_session = model.start_chat()
    st.session_state.chat_history = []


if __name__ == '__main__':
  main()
