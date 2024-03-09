from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
import warnings
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOllama
warnings.filterwarnings('ignore')

def initialization():
    file_path='db'
    llm = Ollama(base_url='http://localhost:11434',model="llama2")
    embeddings=OllamaEmbeddings(model='llama2')
    vectordb=Chroma(persist_directory=file_path,embedding_function=embeddings)
    bot = RetrievalQA.from_chain_type(llm=llm,
                                     chain_type='stuff',
                                     retriever=vectordb.as_retriever(),
                                     return_source_documents=True)
    return bot
def process_llm_response(llm_response):
    response=dict()
    response['result']=llm_response['result']
    metadata=list()
    for source in llm_response['source_documents']:
        metadata.append(source.metadata['source'])
    response['source']=metadata
    return  response
def ask(query:str):
    bot=initialization()
    return process_llm_response(bot(query))
    
# if  __name__=='__main__':
#     query=input("Enter your question")
#     ask(query)