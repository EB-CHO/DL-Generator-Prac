from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# 모델과 프로세서 로드
blip_model_name = "Salesforce/blip2-flan-t5-xl"
blip_processor = BlipProcessor.from_pretrained(blip_model_name)
blip_model = BlipForConditionalGeneration.from_pretrained(blip_model_name)

def generate_image_caption(image_file):
    image = Image.open(image_file)
    inputs = blip_processor(images=image, return_tensors="pt")
    outputs = blip_model.generate(**inputs)
    caption = blip_processor.decode(outputs[0], skip_special_tokens=True)
    return caption
