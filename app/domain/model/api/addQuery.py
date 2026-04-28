from pydantic import BaseModel

class AddQuery(BaseModel):
    query: str