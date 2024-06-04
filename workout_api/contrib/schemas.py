from pydantic import BaseModel, UUID4, Field
from sqlalchemy import DateTime
from typing import Annotated

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        form_attributes = True

class OutMixing(BaseSchema):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[datetime, Field(description='Data de criacao')] 