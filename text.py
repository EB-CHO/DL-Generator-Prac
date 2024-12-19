import openai
import streamlit as st

@st.cache_data(persist=True)
def generate_story_from_text(user_input):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative story generator."},
                {"role": "user", "content": user_input}
            ]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        raise Exception(f"OpenAI API call failed: {e}")

