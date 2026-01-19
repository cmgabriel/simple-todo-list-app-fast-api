# Import BaseModel for schema creation and Field for adding metadata/validation
from pydantic import BaseModel, Field
# Import datetime for handling ISO-formatted date strings
from datetime import datetime
# Import Optional for fields that can be null or missing
from typing import Optional

# The core Data Transfer Object (DTO) representing a Task in the system
class Tasks(BaseModel):
    # The database ID; Optional because it's not provided by the client when creating
    id: Optional[int]
    # Required string with metadata for documentation
    title: str = Field(description="Task Title")
    # Required string with metadata for documentation
    description: str = Field(description="Task Description")
    # Date-time field for the record creation timestamp
    created_on: datetime
    # Date-time field for the last update timestamp
    updated_on: datetime
    # Boolean flag indicating the status of the task
    is_completed: bool

# Schema for the incoming JSON when creating a new task
# Restricted to only the fields a user is allowed to set manually
class NewTaskRequest(BaseModel):
    title: str = Field(description="Task Title")
    description: str = Field(description="Task Description")

# Schema returned after a successful creation
# Inherits from Tasks to include all fields (id, timestamps, etc.)
class NewTaskResponse(Tasks):
    pass

# Schema for the list endpoint (GET /tasks)
# Wraps a list of 'Tasks' objects to provide a structured JSON response object
class GetAllTasksResponse(BaseModel):
    tasks: list

# Schema returned when fetching a specific task by ID
class GetTaskByIdResponse(Tasks):
    pass

# Schema for the update endpoint (PUT /tasks/{id})
# Allows the user to modify the title, description, or completion status
class UpdateTaskByIdRequest(BaseModel):
    title: str = Field(description="Task Title")
    description: str = Field(description="Task Description")
    is_completed: bool
    
# Schema returned after a successful update
class UpdateTaskByIdResponse(Tasks):
    pass