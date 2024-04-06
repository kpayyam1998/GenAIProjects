""""
    This file have chroma DB connections

"""

import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma

from src.helper import load_repo,text_splitter,repo_ingestion,load_embedding

load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

documents=load_repo("repo/")
text_chunks=text_splitter(documents)
embeddings=load_embedding()


# Store vector to vectorDB
vectordb=Chroma.from_documents(text_chunks,embedding=embeddings,persist_directory="./db")

vectordb.persist()