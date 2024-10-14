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
    result = generate_embeddings(client(), "In the example below we're calling the embedding model once per every item that we want to embed. When working with large embedding projects you can alternatively pass the model an array of inputs to embed rather than one input at a time. When you pass the model an array of inputs the max number of input items per call to the embedding endpoint is 2048.")
    print(result)