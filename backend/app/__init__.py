from sqlalchemy import text
from .database import engine


def init_db():

    create_table_query = """
    CREATE TABLE IF NOT EXISTS datasets (
        id SERIAL PRIMARY KEY,
        filename TEXT,
        rows INTEGER,
        columns INTEGER,
        best_model TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with engine.connect() as connection:
        connection.execute(text(create_table_query))
        connection.commit()


if __name__ == "__main__":
    init_db()