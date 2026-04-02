from app.services.chunking import chunk_text
from app.services.summarizer import summarize


def rag_summarize(text, query=None):
    """
    Simplified pipeline (no FAISS / embeddings)
    """

    chunks = chunk_text(text)

    # Smart selection (basic logic)
    if query:
        # select chunks containing keywords
        selected_chunks = [c for c in chunks if query.lower() in c.lower()]
        if not selected_chunks:
            selected_chunks = chunks[:3]
    else:
        selected_chunks = chunks[:3]

    combined_text = " ".join(selected_chunks)

    summary = summarize(combined_text)

    return summary


# 🔹 Test
if __name__ == "__main__":
    text = """
    Artificial Intelligence is transforming industries across the globe.
    Machine learning helps in predictive analytics and automation.
    AI is widely used in healthcare and finance.
    """

    query = "Where is AI used?"

    print(rag_summarize(text, query))