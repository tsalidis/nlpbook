import os

os.environ["USE_TF"] = "0"

from transformers import pipeline

generator = pipeline("text-generation", model="openai-community/gpt2")
result = generator("The Natural Language Processing ", truncation=True)
print(result[0]["generated_text"])
