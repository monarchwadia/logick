from time import sleep
from typing import Generator

class LogickBase:
    def __init__(self):
        pass
    
    def respond(self, user_input: str) -> Generator:
        for chunk in user_input:
            yield chunk
            sleep(0.05)

if __name__ == "__main__":
    logick = LogickBase()
    for chunk in logick.respond("Hello World. It is a lovely, lovely day."):
        print(chunk, end="", flush=True)