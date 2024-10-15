import os
from openai import AzureOpenAI

# TODO: Add test cases for each function

def generate_embeddings(client: AzureOpenAI, text: str):
    return client.embeddings.create(input=[text], model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")).data[0].embedding

def client():
    return AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )

def get_doc_embeddings(chunks: list[str]) -> list[list]:
    client = client()
    return [generate_embeddings(client, chunk) for chunk in chunks]



if __name__ == "__main__":
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())

    result = generate_embeddings(client(), "pgvector is a PostgreSQL extension that provides support for vector similarity search and nearest neighbor search in SQL.")
    print(result)