import tiktoken

tokenizer = tiktoken.get_encoding('cl100k_base')

def chunk_text(text, max_tokens=500):
    tokens = tokenizer.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i:i+max_tokens]
        chunk_text = tokenizer.decode(chunk_tokens)
        chunks.append({
            "chunk_id": len(chunks) + 1,
            "text": chunk_text
        })
    return chunks
