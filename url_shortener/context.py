from pkg.logger.logger import Logger
from url_shortener.storage.sqllite.storage import Storage
import os

class Context:
    def __init__(self):
        self.Logger = Logger("url_shortener.log")

        sqllite_path = os.getenv("SQLITE_DATABASE")
        self.Storage = Storage(sqllite_path)
        
ctx = Context()

