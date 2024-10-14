from .postgres import Postgres
import logging

# TODO: Add test cases for each function

class DocumentChunk():
    id: str
    document_id: str
    text: str
    embedding: list[float]

    #TODO: finish __init__
    def __init__(self):
        pass

    # TODO: finish __str__
    def __str__(self):
        pass

    def _insert(self):
        sql_template = "INSERT INTO document_chunks (document_id, content, embedding) VALUES (%s, %s, %s);"
        sql_template_values = (self.document_id, self.text, self.embedding)
        try:
            conn = Postgres().connect_to_postgres()
            cur = conn.cursor()
            cur.execute(sql_template, sql_template_values)
            conn.commit()
        except Exception as e:
            logging.error("Failed to execute sql: {}\nError: {}".format(sql_template.replace("%s", "{}").format(sql_template_values), e))
            raise
    
    def _update(this):
        None

    def _delete(this):
        None

    def _query(this):
        None