from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base

class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    rows = Column(Integer)
    columns = Column(Integer)
    uploaded_at = Column(DateTime, default=datetime.utcnow)