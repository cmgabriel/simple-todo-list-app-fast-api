# --------------------------
# database.py
# --------------------------

# Import the function to establish a connection to the database
from sqlalchemy import create_engine

# Import session utilities to handle database transactions and the Session type hint
from sqlalchemy.orm import sessionmaker, Session, declarative_base

# Define the connection string; here, it points to a local SQLite file named 'test.db'
DB_URL = "sqlite:///./test.db"

# Create the Engine instance, which manages the connection pool and dialect (SQLite)
engine = create_engine(DB_URL)

# Configure a session factory; 'autoflush=False' prevents manual changes from hitting the DB 
# until a commit, and 'bind=engine' links this factory to our specific database
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Create a base class for your database models; all your tables will inherit from this
Base = declarative_base()

# Define a utility function to generate all tables in the database
def create_tables():
    # Looks at all classes inheriting from 'Base' and creates the corresponding tables if they don't exist
    Base.metadata.create_all(bind=engine)