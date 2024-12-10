import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

def preprocess_text(text):
    """
    Preprocess input text by removing special characters, stopwords, and extra spaces.
    """
    text = re.sub(r"\W+", " ", text)  # Remove non-word characters
    tokens = text.lower().split()
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    return " ".join(tokens)
