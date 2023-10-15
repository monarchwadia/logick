from ingestor.git import GitIngestor

git_ingestor = GitIngestor()
loader = git_ingestor.from_web("https://github.com/langchain-ai/langchain")

data = loader.load()

print(len(data))