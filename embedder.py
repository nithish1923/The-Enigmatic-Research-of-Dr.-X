from nomic import embed

def generate_embeddings(text_chunks):
    return embed.text(text_chunks)
