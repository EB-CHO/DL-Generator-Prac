import openai
import streamlit as st
from PIL import Image
import base64

@st.cache_data(persist=True)
def generate_image_caption(image_bytes):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    try:
        # 이미지 바이트를 Base64로 인코딩
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')

        # GPT 모델을 사용해 캡션 생성
        prompt = f"Generate a caption for the following image (encoded in Base64): {image_base64}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert image caption generator."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        raise Exception(f"OpenAI API call failed: {e}")

@st.cache_data(persist=True)
def generate_story_from_image_caption(image_caption_with_user_input):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative story generator."},
                {"role": "user", "content": image_caption_with_user_input}
            ]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        raise Exception(f"OpenAI API call failed: {e}")

