## Why this repo
I've been building AI related skills lately, like playing around with AI platforms, LLM models, and learning Langchain.
Try to build something that usable, so RAG is a good start. 

This [post](https://anyblockers.com/posts/building-rag-with-postgres) is a good instruction of how.

### Chucking
This [notebook](https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/a4570f3c4883eb9b835b0ee18990e62298f518ef/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb) is awesome. And [visualisation](https://chunkviz.up.railway.app/) as well, for different type of chunkers.

### Embeddings
An embedding is a vector (list) of floating point numbers. The distance between two vectors measures their relatedness. Small distances suggest high relatedness, and large distances suggest low relatedness.

In this demo, we use Azure OpenAI embedding [model](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models?tabs=python-secure#embeddings-models) `text-embedding-ada-002`.

### Pgvector
For `tsvector` column in table `document_chunk` parsing document, see Postgres doc [here](https://www.postgresql.org/docs/current/textsearch-controls.html#TEXTSEARCH-PARSING-DOCUMENTS).

At the same page, see also:
* `to_tsquery`, for parsing queries;
* `ts_rank`, for ranking search results;
* `ts_headline`, for highlighting results;

An example can be found [here](https://www.enterprisedb.com/blog/what-is-pgvector).

### Questions
1. How to manage outdated documents?