from env_config import load_env_config
from ingestor.git import GitIngestor
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.vectorstores.faiss import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
import os

env_conf = load_env_config()


llm = OpenAI(openai_api_key=env_conf.openai_api_key)
chat_model = ChatOpenAI()
embeddings_model = OpenAIEmbeddings()
git_ingestor = GitIngestor()
loader = git_ingestor.from_web("https://github.com/theskumar/python-dotenv")
document_objects = loader.load()
documents = []
for doc in document_objects:
    documents.append(doc.page_content)
vector_store = FAISS.from_texts(documents, embedding=embeddings_model)
retriever = vector_store.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
    { "context": retriever, "question": RunnablePassthrough() }
    | prompt
    | chat_model
    | StrOutputParser()
)


# loop user input
while True:
    user_input = input(">>>> ")
    print("BOT: ", end="")
    answer = chain.stream(user_input)
    for a in answer:
        print(a, flush=True, end="")
    print("")

answer = chain.stream("Is the blockchain package being used?")

for a in answer:
    print(a, flush=True, end="")

# print(chat_model.predict("hi!"))




# # experiment

# llm = OpenAI(openai_api_key=env_conf.openai_api_key)
# model = ChatOpenAI()
# prompt = ChatPromptTemplate.from_template("Existing is really cool isn't it, {name}?")
# chain = prompt | model
# print(chain.input_schema.schema())
# print(chain.output_schema.schema())

# print(chain.invoke({"name": "John"}))