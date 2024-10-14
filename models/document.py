from postgres import Postgres
from document_source import DocumentSource
import logging
from psycopg2.extras import Json

# TODO: Add test cases for each function

class Document():
    id: str
    title: str
    source: str
    meta: dict # arbitrary fields to filter on

    def __init__(self, title, id=None, source=None, meta={}):
        self.id = id
        self.title = title
        self.source = source
        self.meta = meta
    
    def __str__(self):
        return str({
            "id": self.id,
            "title": self.title,
            "source": self.source,
            "meta": self.meta
        })

    def _insert(self):
        sql_template = "INSERT INTO documents (title, source, meta) VALUES (%s, %s, %s);"
        sql_template_values = (self.title, self.source, Json(self.meta)) # Instruction see: https://www.psycopg.org/docs/extras.html#json-adaptation
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

    def _query(self) -> list:
        # Column order matches the __init__ function parameter's order, for returning a list of documents.
        # For use of 'like', see instruction: https://www.psycopg.org/docs/usage.html#values-containing-backslashes-and-like
        sql_template = "SELECT title, id, source, meta::text from documents WHERE title like %s ESCAPE ''"
        sql_template_values = (self.title,)
        if self.source:
            sql_template += " and source like %s ESCAPE ''"
            sql_template_values += (self.source,)
        if self.meta:
            sql_template += " and meta @> %s"
            sql_template_values += (Json(self.meta),)
        sql_template += " order by created_at desc;"
        conn = Postgres().connect_to_postgres()
        try:
            cur = conn.cursor()
            cur.execute(sql_template, sql_template_values)
            records = cur.fetchall()
            conn.commit()
            return [Document(*r) for r in records]
        except Exception as e:
            logging.error("Failed to execute sql: {}\nError: {}".format(sql_template.replace("%s", "{}").format(sql_template_values), e))
            return None
        finally:
            conn.close()
    
    def _update(self):
        None

    def _delete(self):
        None
        
if __name__ == "__main__":
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    doc = Document(title="test", source="vscode unittest", meta={"creator":"tester"})
    # doc._insert()
    for doc in doc._query():
        print(doc) 
