from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pkg.model.tasks import Task

class Storage:
    def __init__(self, db_path: str):
        self.engine = create_engine(db_path)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create(self, task: Task):
        self.session.add(task)
        self.session.commit() 
        
    def getTasks(self) -> list[Task]:
        return self.session.query(Task).all()

    def update(self, task: Task):
        self.session.query(Task).filter_by(id=task.id).update(task)
        self.session.commit()

    def getByID(self, task_id: int) -> Task:
        return self.session.query(Task).filter_by(id=task_id).first()
    
    def delete(self, task_id: int):
        self.session.query(Task).filter_by(id=task_id).delete()
        self.session.commit()

    