from postgres import Postgres
import logging

# TODO: Add test cases for each function

class DocumentChunk():
    id: str
    document_id: str
    content: str
    embedding: list[float]

    def __init__(self, document_id: str, content: str, embedding: list, id: str=None):
        self.document_id = document_id
        self.content = content
        self.embedding = embedding
        self.id = id

    def __str__(self):
        return str({
            "document_id": self.document_id,
            "content": self.content,
            "embedding": self.embedding,
            "id": self.id,
        })

    def _insert(self):
        sql_template = "INSERT INTO document_chunks (document_id, content, embedding) VALUES (%s, %s, %s);"
        sql_template_values = (self.document_id, self.content, self.embedding)
        conn = Postgres().connect_to_postgres()
        try:
            cur = conn.cursor()
            cur.execute(sql_template, sql_template_values)
            conn.commit()
        except Exception as e:
            logging.error("Failed to execute sql: {}\nError: {}".format(sql_template.replace("%s", "{}").format(sql_template_values), e))
            raise
        finally:
            conn.close()
    
    def _update(this):
        None

    def _delete(this):
        None

    def _query(this):
        None

if __name__ == "__main__":
    from dotenv import find_dotenv, load_dotenv
    load_dotenv(find_dotenv())

    from document import Document
    result = Document(title="pg_trgm")._query()
    doc = result[0] if len(result) > 0 else None

    if doc:
        from services.document_embeddings import client, get_doc_embeddings
        chunk_embedding = DocumentChunk(doc.id, content=doc.source, embedding=get_doc_embeddings(client(), doc.source))
        chunk_embedding._insert()
