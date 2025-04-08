from fastapi import FastAPI
from transformers import T5Tokenizer, T5ForConditionalGeneration

app = FastAPI()

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-small")

@app.get("/generate")
def generate(text: str):
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    return {"output": tokenizer.decode(outputs[0], skip_special_tokens = True)}
