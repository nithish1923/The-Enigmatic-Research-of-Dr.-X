from llama_cpp import Llama
from embedder import generate_embeddings
from vector_db import get_vector_db

llm = Llama(model_path="llama_model.gguf")

def generate_answer(question, retriever):
    q_embedding = generate_embeddings([question])[0]
    results = retriever.similarity_search_by_vector(q_embedding)
    context = "\n".join([doc['text'] for doc in results])
    prompt = f"Context:\n{context}\n\nQ: {question}\nA:"
    response = llm(prompt=prompt, max_tokens=200)
    return response['choices'][0]['text']
