from transformers import CLIPProcessor, CLIPModel
from PIL import Image

# 모델과 프로세서 로드
clip_model_name = "openai/clip-vit-base-patch32"
clip_model = CLIPModel.from_pretrained(clip_model_name)
clip_processor = CLIPProcessor.from_pretrained(clip_model_name)

def generate_image_embedding(image_file):
    image = Image.open(image_file)
    inputs = clip_processor(images=image, return_tensors="pt")
    embedding = clip_model.get_image_features(**inputs)
    return embedding.detach().numpy()
