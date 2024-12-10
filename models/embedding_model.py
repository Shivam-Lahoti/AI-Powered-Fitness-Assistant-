import openai


OPENAI_API_KEY = "your_openai_api_key"

openai.api_key = OPENAI_API_KEY

def get_embeddings(text):
    """
    Generate embeddings for the given text using OpenAI's embedding model.
    
    Args:
        text (str): Input text to be embedded.
    
    Returns:
        list: A vector representation of the text.
    """
    try:
        response = openai.Embedding.create(
            input=text,
            model="text-embedding-ada-002"  # Example embedding model
        )
        return response['data'][0]['embedding']
    except Exception as e:
        print(f"Error generating embeddings: {e}")
        return None
