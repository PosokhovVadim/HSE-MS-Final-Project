from pkg.logger.logger import Logger
from todo_service.storage.sqllite.storage import Storage
import os

class Context:
    def __init__(self):
        self.Logger = Logger("todo_service.log")

        sqllite_path = os.getenv("SQLITE_DATABASE")
        self.Storage = Storage(sqllite_path)
        
ctx = Context()