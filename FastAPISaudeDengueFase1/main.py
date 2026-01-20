import pickle
import pandas as pd
from DengueInput import DengueInput

from fastapi import FastAPI, HTTPException
from DengueResponse import DengueResponse
from ErroReponse import ErroResponse

app = FastAPI()

@app.post("/predict",
          summary="Realiza predição de hospitalizações de dengue. Valores payload: 1-Sim / 2- Não",
          description="Endpoint responsável por receber dados clínicos do paciente e retornar a predição de hospitalização.",
          response_model=DengueResponse,
          responses={
              400: {"model": ErroResponse},
              422: {"model": ErroResponse},
              500: {"model": ErroResponse}
          })
async def run_predict(input: DengueInput):
    """
    Realiza a predição sobre hospitalização do caso de dengue.

    Parâmetros:
        Input (DengueInput): Objeto contendo dados do paciente 1 = Sim, 2 = Não.

    Retorno:
        Resultado da predição.
    """
    try:
        dados = input.model_dump()

        modelo_salvo = pickle.load(open("modelo_hospitalizacao.pkl", "rb"))

        df = pd.DataFrame([dados])

        pred = modelo_salvo.predict(df)[0]
        prob = modelo_salvo.predict_proba(df)[0][0]

        predicao_texto = "Sim" if pred == 1 else "Não"

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail={
                "erro": "Erro de validação",
                "detalhe": str(e)
            }
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "erro": "Erro interno",
                "detalhe": str(e)
            }
        )

    return DengueResponse(
        predicao=interpretar(pred),
        codigo=int(pred),
        probabilidade=float(prob),
        mensagem="Predição realizada com sucesso"
    )

    resultado = modelo_salvo.predict(df)

    return {"predição": str(interpretar(resultado[0]))}

def interpretar(resultado):
    """
        Converte resultado numérico em texto.

        Args:
            valor (float): resultado da predição

        Returns:
            str:
            '1 - Sim, paciente deve ser hospitalizado!'
            ou
            '2 - Não, paciente não deve ser hospitalizado!'
        """

    mensagem = ""
    if resultado == 1.0:
        mensagem =  "1 - Sim, paciente deve ser hospitalizado!"
    else:
        mensagem = "2 - Não, paciente não deve ser hospitalizado!"

    print(mensagem)
    return mensagem