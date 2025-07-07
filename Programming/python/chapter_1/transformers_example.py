import os
os.environ["USE_TF"] = "0"


from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
result = generator("The Natural Language Processing ", max_length=30, num_return_sequences=1)
print(result[0]["generated_text"])
