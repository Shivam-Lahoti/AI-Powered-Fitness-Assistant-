from vector_database.semantic_search import search_pinecone
from models.llm_integration import generate_response

def process_query(query):

    # Perform semantic search to retrieve relevant documents
    search_results = search_pinecone(query)
    context = " ".join([res['metadata']['text'] for res in search_results['matches']])

    # Generate the final response using the LLM
    answer = generate_response(query, context)
    return answer
