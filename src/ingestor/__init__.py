from git import Repo
from langchain.document_loaders import GitLoader
from tempfile import TemporaryDirectory

def git_loader_from_disk(repo_path: str, branch: str):
    return GitLoader(repo_path=repo_path, branch=branch)

def git_loader_from_web(url: str):
    # create temp directory
    with TemporaryDirectory() as tmpdirname:
        repo = Repo.clone_from(url, to_path=tmpdirname)
        branch = repo.head.reference
        return git_loader_from_disk(tmpdirname, branch)

