# generation.py

from transformers import pipeline

# Load a basic text-generation model (e.g., GPT-2)
generator = pipeline("text-generation", model="gpt2")

def generate_response(domain_or_query, prompt=None):
    """
    If prompt is provided, use it for text generation (backend API).
    If only domain_or_query is given, use it for Streamlit (frontend).
    """
    input_text = prompt if prompt else domain_or_query

    generated = generator(input_text, max_length=200, num_return_sequences=1)
    return generated[0]['generated_text']
