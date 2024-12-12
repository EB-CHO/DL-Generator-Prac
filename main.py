import streamlit as st

from workflow_text_to_text import generate_story_from_text
from workflow_image_to_text import generate_image_caption, generate_story_from_image_caption

st.set_page_config(
    page_title="AI Story Generator", layout="wide", page_icon="📖"
)

st.markdown(
    """
    <h1 style='text-align: center; color: #FF4500;'>My AI Storyteller 📚</h1>
    """, 
    unsafe_allow_html=True
)

with st.expander("🔍 About this app", expanded=False):
    st.markdown(
        """
        <p style='font-size:16px; color:#555;'>
        This app uses the <b>Clarifai AI</b> engine to generate stories based on the input you provide using <b>LLM</b> models. 
        You can either upload an image or enter some text to get started. 
        The story will be generated based on the theme you choose, which can be selected from the sidebar.
        </p>
        """,
        unsafe_allow_html=True
    )

st.sidebar.markdown("### Select the genre/theme of the story:")

story_theme = st.sidebar.radio("Genre", ("Horror 👻", "Action 🏃‍♂️", "Romance ❤️", "Comedy 😂", "Historical ⏳"))
selected_theme = story_theme.split()[0].strip()  # Extract theme text without emojis

theme_based_prompts = {
    "Horror": "Write a horror story that ends mysteriously using: ",
    "Action": "Write a story with lots of action using: ",
    "Romance": "Write a romantic story using: ",
    "Comedy": "Write a funny story using: ",
    "Historical": "Write a story based on a historical event with the help of the input: ",
    "Science Fiction": "Write a science fiction story using: "
}

st.markdown("## Choose the input type for generating the story")

input_type = st.radio("Input type", ("Text ✏️", "Image 🖼️"))

if input_type == "Text ✏️":
    st.markdown("### Enter the sentences you want to have your story revolve around:")

    input_text = st.text_area(
        "Enter the text here",
        height=100,
        value="As the rain poured down on a quiet, dimly lit street, I found myself standing in front of a quaint bookstore"
    )

    # Ensure theme-based input is defined
    if selected_theme in theme_based_prompts:
        theme_based_input = theme_based_prompts[selected_theme] + " " + input_text
    else:
        theme_based_input = ""
        st.error("Selected theme is invalid. Please select a valid theme.")

    st.write("Generated Theme-based Input:", theme_based_input)  # Debugging

    if st.button("🚀 Generate story"):
        if theme_based_input:
            with st.spinner("Generating your story... Please wait about 30-40 seconds."):
                try:
                    story = generate_story_from_text(theme_based_input)
                    st.write("Generated Story:", story)  # Debugging
                    if story.strip():
                        story_lines = story.split('\n')
                        formatted_story = "\n".join(["##### " + line for line in story_lines])
                    else:
                        formatted_story = "No story was generated. Please try again."
                except Exception as e:
                    st.error(f"Error generating story: {e}")
                    formatted_story = "Error occurred while generating the story."
            
            with st.expander("📖 View story", expanded=True):
                st.markdown(formatted_story)


