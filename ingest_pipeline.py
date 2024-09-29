from models import document, document_chunk
from services import chunk_data

def ingest():
    raw_data = extract_data_from_source()
    clean_data = process_and_clean_data(raw_data)
    chunks = chunk_data(clean_data)
    chunk_embeddings = embed_chunks(chunks)
    document_chunks = zip(chunks, chunk_embeddings)
    insert_document_chunks(document_chunks)