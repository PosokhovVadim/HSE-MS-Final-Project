from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pkg.model.urls import ShortURL

class Storage:
    def __init__(self, db_path: str):
        self.engine = create_engine(db_path)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        # self.Base.metadata.create_all(self.engine) need it?

    def save(self, url: ShortURL):
        self.session.add(url)
        self.session.commit() 
        
    def get(self, short_id: str) -> ShortURL:
        return self.session.query(ShortURL).filter_by(short_id=short_id).first()

    def delete(self, short_id: str):
        self.session.query(ShortURL).filter_by(short_id=short_id).delete()
        self.session.commit()

    