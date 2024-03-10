# __(O_O) Q&A Chatbot For PDF Document (O_O) __

![Chatbot](https://miro.medium.com/v2/resize:fit:1400/0*Iy9LzhTAPht6ghwU.png)
This Respository contain a Flet(Flutter Application) that utilizes the LangChain and Ollama (openSource LLM Model as llama2) language model to create a conversational Q&A chatbot. The chatbot is designed to answer questions about the content of PDF document

## Table of  Contents
- [Q&A Chatbot for PDF  Document](#qa-chatbot-for-pdf-document)

    -[Table of Contents](#table-of-contents)

    -[Installation](#installation)
    
    -[Usage](#usage)

    -[Architecture](#architecture)

    -[License](#license)

    -[Contact](#contact)




## Installation

Before starting, make sure you have Python 3.8+ installed. To run the Q&A Chatbot, follow these steps:
1. Create Conda Env :
 ```
 conda create --name pdf_env python
 ```
1. Clone this repository:
```
git clone  https://github.com/GENRATECODE/pdf_chatbot.git
cd pdf_chatbot
```
2. Install the necessary Libraries:
```
pip install -r requirements.txt
```
3. Install Ollama
```
https://ollama.com/download
```

## Usage
 Dwonload LLM Model on Local Own System
```
ollama pull llama2
```
Run the application from your terminal with:
```
flet app.py
```
or 
```
python app.py
```
if Upload a pdf file and ask question about its content. The chatbot will generate answers based  on the context of the PDF.

docs/python1.pdf
copy and paste in ```docs``` folder
then run vectordb_embedding.py file 

```
python vectorDB_Embedding.py
```

## Architecture
![Architecture Diagram](images/arche.png)

#### Steps

 1. First Gather PDF file in docs.

 2.  ```langchain.Directory('docs',glob='./pdf',loader_cls=PyPDFLoader)``` using this function load pdf in variable
 3. Using ```RecursiveCharacterTextSplitter``` function Split pdf file into chunks (book -> pages )
 4. Splited file embedding using this function ```OllamaEmbeddings(model='llama2')``` convert into numeric form to save Chromadb(OpenSource VectorDatabase)
 5. ```Chroma.from_documents(documents=text_split,embeddings,persist_directory=persist_dirrectory)``` save chunk file into vectordb and ```vectordb.persist()``` store value in local disk 

 6. Make a Retriever  Object for each chunk of text,
 ```retriever.as_retriever()```
 7. LLM model ```Ollama(base_url='http:/localhost:11434',model="llama2")```
 8. RAG Chain use ```from langchain.chains import RetrievalQA``` function RAG 
 ```
 qa_gen=RetrievalQA.from_chain_type(llm=llm_llama,
                      chain_type="stuff",
                      retriever=retriever,
                      return_source_documents=True)
````
9.  **Query**

```
 qa_gen(question)['result'] 

```

## License
This  project is licensed under the MIT License -


## Contact
For more information, feel free to reach out!

    -Abhay Swarnkar
    -Email: abhayswarnakar@gmail.com
    
-[Linkedin](https://www.linkedin.com/in/bhayswarnakarml/)

## Output

![Output](images/output1.png)

![bot-reply](images/final%20output.png)

## Issuse During Installation Chromadb 

```
uilding wheel for hnswlib (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Building wheel for hnswlib (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [21 lines of output]
      running bdist_wheel
      running build
      running build_ext
      creating tmp
      x86_64-linux-gnu-gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -fPIC -I/home/namanc/codes/langchian_chromadb/venv/include -I/usr/include/python3.10 -c /tmp/tmp822lkln8.cpp -o tmp/tmp822lkln8.o -std=c++14
      x86_64-linux-gnu-gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -fPIC -I/home/namanc/codes/langchian_chromadb/venv/include -I/usr/include/python3.10 -c /tmp/tmpw33wg22s.cpp -o tmp/tmpw33wg22s.o -fvisibility=hidden
      building 'hnswlib' extension
      creating build
      creating build/temp.linux-x86_64-cpython-310
      creating build/temp.linux-x86_64-cpython-310/python_bindings
      x86_64-linux-gnu-gcc -pthread -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -fPIC -I/tmp/pip-build-env-izlfj5h4/overlay/lib/python3.10/site-packages/pybind11/include -I/tmp/pip-build-env-izlfj5h4/overlay/lib/python3.10/site-packages/numpy/core/include -I./hnswlib/ -I/home/namanc/codes/langchian_chromadb/venv/include -I/usr/include/python3.10 -c ./python_bindings/bindings.cpp -o build/temp.linux-x86_64-cpython-310/./python_bindings/bindings.o -O3 -fopenmp -DVERSION_INFO=\"0.7.0\" -std=c++14 -fvisibility=hidden
      In file included from /tmp/pip-build-env-izlfj5h4/overlay/lib/python3.10/site-packages/pybind11/include/pybind11/detail/../attr.h:13,
                       from /tmp/pip-build-env-izlfj5h4/overlay/lib/python3.10/site-packages/pybind11/include/pybind11/detail/class.h:12,
                       from /tmp/pip-build-env-izlfj5h4/overlay/lib/python3.10/site-packages/pybind11/include/pybind11/pybind11.h:13,
                       from /tmp/pip-build-env-izlfj5h4/overlay/lib/python3.10/site-packages/pybind11/include/pybind11/functional.h:12,
                       from ./python_bindings/bindings.cpp:2:
      /tmp/pip-build-env-izlfj5h4/overlay/lib/python3.10/site-packages/pybind11/include/pybind11/detail/../detail/common.h:266:10: fatal error: Python.h: No such file or directory
        266 | #include <Python.h>
            |          ^~~~~~~~~~
      compilation terminated.
      error: command '/usr/bin/x86_64-linux-gnu-gcc' failed with exit code 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for hnswlib
Failed to build hnswlib
ERROR: Could not build wheels for hnswlib, which is required to install pyproject.toml-based projects
````
Resolve this error in windows install 

```
https://visualstudio.microsoft.com/visual-cpp-build-tools/

istall this package from this link
more detail serach 
```
https://stackoverflow.com/questions/76592197/python-installation-of-chromadb-failing
```
