import os
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownTextSplitter, PythonCodeTextSplitter, Language
from unstructured.partition.pdf import partition_pdf
from unstructured.staging.base import elements_to_json

# TODO: apply .env chunking config
# TODO: chunking JSON?

# For RecursiveCharacterTextSplitter splitters, see: https://github.com/langchain-ai/langchain/blob/9ef2feb6747f5a69d186bd623b569ad722829a5e/libs/langchain/langchain/text_splitter.py#L842
# RecursiveCharacterTextSplitter have method from_language(), with wide range of language options
# For MarkdownTextSplitter splitters, see: https://github.com/langchain-ai/langchain/blob/9ef2feb6747f5a69d186bd623b569ad722829a5e/libs/langchain/langchain/text_splitter.py#L1175
# For PythonCodeTextSplitter splitters, see: https://github.com/langchain-ai/langchain/blob/9ef2feb6747f5a69d186bd623b569ad722829a5e/libs/langchain/langchain/text_splitter.py#L1069
def chunk_data(data: str, doc_type: str = "text") -> List[str]:
    if doc_type.lower() == "markdown":
        # splitter = MarkdownTextSplitter(chunk_size=40, chunk_overlap=0)
        splitter = RecursiveCharacterTextSplitter.from_language(
            language=Language.MARKDOWN, chunk_size=256, chunk_overlap=32
        )
    elif doc_type.lower() == "python":
        # splitter = PythonCodeTextSplitter(chunk_size=40, chunk_overlap=0)
        splitter = RecursiveCharacterTextSplitter.from_language(
            language=Language.PYTHON, chunk_size=256, chunk_overlap=32
        )
    elif doc_type.lower() in ["js", "javascript"]:
        splitter = RecursiveCharacterTextSplitter.from_language(
            language=Language.JS, chunk_size=256, chunk_overlap=32
        )
    elif doc_type.lower() == "pdf":
        elements = partition_pdf(
            file=data,
            # Unstructured Helpers
            strategy="hi_res", 
            infer_table_structure=True, 
            model_name="yolox"
        )
    else:
        splitter = RecursiveCharacterTextSplitter(chunk_size=450, chunk_overlap=32)
    
    try:
        chunks = splitter.create_documents([data])
    except Exception:
        chunks = [ele.metadata.text_as_html for ele in elements]
        # print(elements_to_json(elements))
    return chunks





if __name__ == "__main__":
    simple_text = """
        One of the most important things I didn't understand about the world when I was a child is the degree to which the returns for performance are superlinear.

        Teachers and coaches implicitly told us the returns were linear. "You get out," I heard a thousand times, "what you put in." They meant well, but this is rarely true. If your product is only half as good as your competitor's, you don't get half as many customers. You get no customers, and you go out of business.

        It's obviously true that the returns for performance are superlinear in business. Some think this is a flaw of capitalism, and that if we changed the rules it would stop being true. But superlinear returns for performance are a feature of the world, not an artifact of rules we've invented. We see the same pattern in fame, power, military victories, knowledge, and even benefit to humanity. In all of these, the rich get richer. [1]
        """
    # for chuck in chunk_data(simple_text, "text"):
    #     print(chuck)

    markdown_text = """
        # Fun in California

        ## Driving

        Try driving on the 1 down to San Diego

        ### Food

        Make sure to eat a burrito while you're there

        ## Hiking

        Go to Yosemite
        """
    # for chuck in chunk_data(markdown_text, "markdown"):
    #     print(chuck)

    python_text = """
        class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        p1 = Person("John", 36)

        for i in range(10):
            print (i)
        """
    # for chuck in chunk_data(python_text, "python"):
    #     print(chuck)

    javascript_text = """
        // Function is called, the return value will end up in x
        let x = myFunction(4, 3);

        function myFunction(a, b) {
        // Function returns the product of a and b
        return a * b;
        }
        """
    # for chuck in chunk_data(javascript_text, "javascript"):
    #     print(chuck)

    filename = "static/SalesforceFinancial.pdf"
    # with open(file=filename, mode="rb") as pdf_data:
    #     for chuck in chunk_data(pdf_data, "pdf"):
    #         print(chuck)