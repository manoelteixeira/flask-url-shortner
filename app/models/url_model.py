from datetime import datetime
from app import db 

class Url(db.Model):
    __tablename__ = "url"
    
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), index=True, unique=False, nullable=False)
    key = db.Column(db.String(), index=True, unique=False, nullable=False)
    created_at = db.Column(db.DateTime(), index=True, unique=False, nullable=False)
    
    def __init__(self, url:str, key:str) -> None:
        self.url = url
        self.key = key
        self.created_at = datetime.utcnow()
        
    def __repr__(self) -> str:
        return f"<id: {self.id} - key: {self.key} - created at: {self.created_at.date()}>"
        