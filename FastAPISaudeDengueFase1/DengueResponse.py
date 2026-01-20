from pydantic import BaseModel, Field

class DengueResponse(BaseModel):
    predicao: str = Field(
        ...,
        description="Resultado textual da predição",
        example="Sim"
    )

    codigo: int = Field(
        ...,
        description="Código numérico retornado pelo modelo (1 ou 2)",
        example=1
    )

    probabilidade: float = Field(
        ...,
        description="Probabilidade estimada pelo modelo",
        example=0.87
    )

    mensagem: str = Field(
        ...,
        description="Mensagem explicativa do resultado",
        example="Alta probabilidade de hospitalização"
    )

