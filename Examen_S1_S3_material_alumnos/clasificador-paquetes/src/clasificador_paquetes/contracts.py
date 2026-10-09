from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, field_validator

class Entrada(BaseModel):
    # TODO
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    id_paquete: str = Field(min_length=1, str_strip_whitespace=True)#el str_strip, encontrado en internet
    peso_kg: float = Field(gt=0, le=30)
    distancia_km: float = Field(ge=0, le=200)


class Salida(BaseModel):
    # TODO
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    id_paquete: str = Field(min_length=1)
    categoria: Literal["normal", "urgente"]
    confianza: float = Field(ge=0, le=1)
