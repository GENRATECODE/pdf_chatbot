from langchain.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
import warnings
warnings.filterwarnings('ignore')

def vectordb_function():
    # if you want change persist directory then change 'db'  to ' desire_directory'
    persist_dirrectory='db'
    # same location of persist_directory in load chroma(vectordb) in chatbot_function.py
    # pdf file location to desire location 'doc' to 'another_location'
    #'docs' to change 'data'
    file_loacation='docs'
    # Load Document
    loader=DirectoryLoader(file_loacation,glob='./*.pdf',loader_cls=PyPDFLoader)
    docs=loader.load()
    
    # divide into chunks
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
    texts=text_splitter.split_documents(docs)
    # creating embedding variable use llama2 model who develope by facebook 7B to 70B
    embeddings=OllamaEmbeddings(model='llama2')
    # Create Vector Database
    vectordb=Chroma.from_documents(documents=texts,embedding=embeddings,persist_directory=persist_dirrectory)
    vectordb.persist()
    vectordb=None
    
if  __name__=='__main__':
    vectordb_function()