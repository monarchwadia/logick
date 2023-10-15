from urllib.parse import urlparse
from git import Repo
from langchain.document_loaders import GitLoader
import os

class GitIngestor():
    def from_disk(self, folder_path: str):
        print("Loading repo from disk path:", folder_path)
        branch = Repo(folder_path).active_branch.name
        return GitLoader(repo_path=folder_path, branch=branch)

    def from_web(self, url: str):
        print("Loading repo from web:", url)
        cache_dir = self.__build_cache_dirname(url)
        # if cache directory does not exist, create it

        if os.path.exists(cache_dir):
            print("Cache directory exists:", cache_dir)
        else:
            os.makedirs(cache_dir, exist_ok=True)
            print("Created cache directory:", cache_dir)
            print("Cloning repo from:", url)
            Repo.clone_from(url, to_path=cache_dir)
            print("Successfully cloned to:", cache_dir)

        return self.from_disk(cache_dir)

    
    def __build_cache_dirname(self, url: str):
        parsed_url = urlparse(url)
        namespace = parsed_url.path.strip('/').split('/')[-2:]
        cache_dir = os.path.join('.cache', *namespace)
        return cache_dir