from app.core.database import engine, Base
from app.models.dataset_model import Dataset

def init():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init()