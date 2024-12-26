from pkg.logger.logger import Logger
import os

class Context:
    def __init__(self):
        self.Logger = Logger("todo_service.log")

        # init db connection
        sqllite_path = os.getenv("SQLITE_DATABASE")

ctx = Context()