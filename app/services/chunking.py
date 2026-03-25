def chunk_text(text, chunk_size=50):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))

    return chunks


if __name__ == "__main__":
    text = "This is a sample text " * 100
    chunks = chunk_text(text)

    print(f"Total chunks: {len(chunks)}")
    print(chunks[0])