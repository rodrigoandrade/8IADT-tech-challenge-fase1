from pydantic import BaseModel, Field

class ErroResponse(BaseModel):
    erro: str = Field(..., description="Tipo do erro ocorrido", example="Erro de validação")
    detalhe: str = Field(..., description="Descrição detalhada do erro", example="Campo FEBRE inválido")
