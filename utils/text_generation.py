from transformers import GPTNeoForCausalLM, AutoTokenizer

# 모델과 토크나이저 로드
model_name = "EleutherAI/gpt-neo-2.7B"
model = GPTNeoForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def generate_text(prompt, max_length=200):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(inputs.input_ids, max_length=max_length, num_return_sequences=1, temperature=0.7)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
