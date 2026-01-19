# Import the Base class (the registry for all models) from your local database configuration
from database import Base
# Import specific SQLAlchemy types and constructs for defining table columns
from sqlalchemy import Boolean, Column, Integer, String, DateTime, text

# Define the TaskDB class; it inherits from Base to be recognized by SQLAlchemy's ORM
class TaskDB(Base):
    # Set the actual name of the table in the database (e.g., SQLite/PostgreSQL)
    __tablename__ = "tasks"
    
    # Primary key column: unique identifier for each task; 'index=True' speeds up lookups
    id = Column(Integer, primary_key=True, index=True)
    
    # String column for the title; indexed for faster searching by name
    title = Column(String, index=True)
    
    # String column for the detailed task description (unindexed)
    description = Column(String)
    
    # Timestamp for creation; 'server_default' lets the database handle the time generation
    created_on = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    
    # Timestamp for updates; 'server_onupdate' tells the DB to refresh this every time the row changes
    updated_on = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    
    # Boolean flag; defaults to 'False' (incomplete) when a new row is inserted
    is_completed = Column(Boolean, default=False)