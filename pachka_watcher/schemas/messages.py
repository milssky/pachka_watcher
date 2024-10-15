from pydantic import BaseModel


class File(BaseModel):
    id: int
    key: str
    name: str
    file_type: str  # Enum
    url: str


class Thread(BaseModel):
    id: int
    chat_id: int


class Message(BaseModel):
    id: int
    entity_type: str  # Enum
    entity_id: int
    chat_id: int
    content: str
    user_id: int
    created_at: str
    files: list[File]
    thread: Thread | None 
    parent_message_id: int | None