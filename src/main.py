from env_config import load_env_config
from ingestor.git import GitIngestor
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import os

env_conf = load_env_config()


llm = OpenAI(openai_api_key=env_conf.openai_api_key)
chat_model = ChatOpenAI()

# print(chat_model.predict("hi!"))

git_ingestor = GitIngestor()
data = git_ingestor.from_web("https://github.com/theskumar/python-dotenv")
print("Number of files read: ", data)