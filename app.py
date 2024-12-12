import streamlit as st
from utils.text_generation import generate_text
from utils.image_embedding import generate_image_embedding
from utils.image_captioning import generate_image_caption

# 페이지 설정
st.set_page_config(page_title="Story Generator", layout="wide")

st.title("✍️Story Generator with Text and Image✍️")
st.subheader("Enter a text prompt and upload an image to generate a story!")

# 사용자 입력
text_input = st.text_area("Enter your text prompt:")
uploaded_image = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])

if st.button("Generate Story➡️"):
    if text_input and uploaded_image:
        # 이미지 캡션 생성
        caption = generate_image_caption(uploaded_image)
        st.write(f"**Image Caption:** {caption}")
        
        # 이미지 임베딩 생성
        embedding = generate_image_embedding(uploaded_image)
        st.write("Image embedding generated successfully.")
        
        # 텍스트 기반 스토리 생성
        story = generate_text(text_input + " " + caption)
        st.subheader("Generated Story")
        st.write(story)
    else:
        st.warning("Please provide both text and an image!")
