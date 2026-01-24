from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

CATEGORIES = ["Electronics", "Home", "Fashion", "Beauty", "Sports"]

def map_attributes(text):
    result = classifier(text, CATEGORIES)
    return {
        "category": result["labels"][0],
        "confidence": result["scores"][0]
    }
