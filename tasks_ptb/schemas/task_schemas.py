from datetime import datetime

from pydantic import BaseModel, field_validator


class UpdateTaskDTO(BaseModel):
    desc: str
    deadline: datetime
    completed: bool

    @field_validator("deadline", mode="before")
    def validate_deadline(cls, value):
        # Clean up the input
        if isinstance(value, str):
            value = value.strip().strip('"')  # Remove quotes and whitespace
        return datetime.fromisoformat(value)  # Convert to datetime

    @field_validator("completed", mode="before")
    def validate_completed(cls, value):
        # Clean up the input
        if isinstance(value, str):
            value = value.strip().strip('"')  # Remove quotes and whitespace
        return bool(int(value))  # Convert to bool


class TaskDTO(UpdateTaskDTO):
    user_id: int
