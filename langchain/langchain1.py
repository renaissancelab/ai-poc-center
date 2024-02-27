#!/usr/bin/env python3

import os
import getpass
from langchain.embeddings.openai import OpenAIEmbeddings

os.environ['OPENAI_API_KEY'] = getpass.getpass('OpenAI API Key:')

# AttributeError: module 'openai' has no attribute 'error'

if __name__ == '__main__':
    embeddings = OpenAIEmbeddings()
    text = "This is a test document."
    query_result = embeddings.embed_query(text)
    doc_result = embeddings.embed_documents([text])