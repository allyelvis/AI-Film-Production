from transformers import pipeline

# Load the model pipeline
generator = pipeline("text-generation", model="gpt-neo-2.7B")

# Generate a script segment
prompt = "A tense scene where the protagonist confronts the villain"
script = generator(prompt, max_length=200, do_sample=True, temperature=0.8)

print("Generated Script:\n", script[0]['generated_text'])
