from sentence_transformers import SentenceTransformer

# Load model once (important for performance)
model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embeddings(text_chunks):
    """
    Convert list of text chunks into embeddings
    """
    embeddings = model.encode(text_chunks)
    return embeddings