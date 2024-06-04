from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do contro de treinamento', example='CT King', max_lenght=20)]
    endereco: Annotated[str, Field(description='Endereco do contro de treinament/o', example='Rua X, 002', max_lenght=60)]
    propietario: Annotated[str, Field(description='Propietário do contro de treinamento', example='Marcos', max_lenght=30)]