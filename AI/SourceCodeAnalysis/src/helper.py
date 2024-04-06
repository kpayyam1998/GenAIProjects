"""
    This file have loder,split_document,chunking,embedding functions

"""

import os

from git import Repo
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.text_splitter import Language
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings

# Clone repo
def repo_ingestion(repo_path_url):
    os.makedirs("repo/",exist_ok=True) #it will create directory name as repo
    repo_path="repo/"
    Repo.clone_from(repo_path_url,to_path=repo_path)

# Loading repo as document
def load_repo(repo_path):
    loader=GenericLoader.from_filesystem(repo_path,
                                  glob="**/*",
                                  suffixes=".py",
                                  parser=LanguageParser(language=Language.PYTHON,parser_threshold=500)
                                  )
    documents=loader.load()
    return documents

# Creating Chunks
def text_splitter(documents):
    document_splitter=RecursiveCharacterTextSplitter.from_language(language=Language.PYTHON,
                                                 chunk_size=2000,
                                                 chunk_overlap=200)
    text_chunks=document_splitter.split_documents(documents)

    return text_chunks

# Loading Embedding
def load_embedding():
    embeddings=OpenAIEmbeddings()
    return embeddings

                                                 
