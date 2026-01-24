from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="EleutherAI/gpt-j-6B",
    device=0 if False else -1  # CPU demo
)

def generate_listing(title, description):
    prompt = f"""
    Product: {title}
    Description: {description}

    Generate:
    1. Amazon SEO title
    2. 5 bullet points
    3. Viral TikTok caption
    """

    result = generator(prompt, max_length=250, do_sample=True)
    return result[0]["generated_text"]
