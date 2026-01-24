from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",
    device=-1  # CPU
)

def generate_listing(title, description):
    prompt = f"""
Generate:
- Amazon SEO title
- 3 bullet points
- TikTok caption

Product title: {title}
Description: {description}
"""

    result = generator(prompt, max_length=150)
    return result[0]["generated_text"]
