import pickle
import pandas as pd
from DengueInput import DengueInput

from fastapi import FastAPI
app = FastAPI()

@app.post("/predict")
async def run_predict(input: DengueInput):

    dados = input.model_dump()

    modelo_salvo = pickle.load(open("modelo_hospitalizacao.pkl", "rb"))

    df = pd.DataFrame([dados])
    resultado = modelo_salvo.predict(df)

    return {"predição": str(interpretar(resultado[0]))}

def interpretar(resultado):
    mensagem = ""
    if resultado == 1.0:
        mensagem =  "1 - Sim, paciente deve ser hospitalizado!"
    else:
        mensagem = "2 - Não, paciente não deve ser hospitalizado!"
    print(mensagem)
    return mensagem

def registro_cenario_hospitalizacao():
    registro = {
        "FEBRE": 1.0,
        "MIALGIA": 2.0,
        "CEFALEIA": 1.0,
        "VOMITO": 2.0,
        "NAUSEA": 1.0,
        "DOR_COSTAS": 2.0,
        "ARTRALGIA": 2.0,
        "DOR_RETRO": 2.0,
        "RESUL_SORO": 1.0,
        "RESUL_NS1": 2.0,
        "EVOLUCAO": 1.0,
        "ALRM_HIPOT": 2.0,
        "ALRM_PLAQ": 1.0,
        "ALRM_VOM": 2.0,
        "ALRM_SANG": 2.0,
        "ALRM_HEMAT": 2.0,
        "ALRM_ABDOM": 2.0,
        "ALRM_LETAR": 2.0,
        "ALRM_HEPAT": 2.0,
        "ALRM_LIQ": 2.0,
        "GRAV_PULSO": 2.0,
        "GRAV_CONV": 2.0,
        "GRAV_ENCH": 2.0,
        "GRAV_INSUF": 2.0,
        "GRAV_TAQUI": 2.0,
        "GRAV_EXTRE": 2.0,
        "GRAV_HIPOT": 2.0,
        "GRAV_HEMAT": 2.0,
        "GRAV_MELEN": 2.0,
        "GRAV_CONSC": 2.0,
        "GRAV_ORGAO": 2.0
    }

    return registro

def registro_cenario_nao_hospitalizacao():
    registro = {
        "FEBRE": 1.0,
        "MIALGIA": 1.0,
        "CEFALEIA": 1.0,
        "VOMITO": 2.0,
        "NAUSEA": 2.0,
        "DOR_COSTAS": 1.0,
        "ARTRALGIA": 1.0,
        "DOR_RETRO": 1.0,
        "RESUL_SORO": 1.0,
        "RESUL_NS1": 4.0,
        "EVOLUCAO": 1.0,
        "ALRM_HIPOT": 2.0,
        "ALRM_PLAQ": 2.0,
        "ALRM_VOM": 2.0,
        "ALRM_SANG": 2.0,
        "ALRM_HEMAT": 2.0,
        "ALRM_ABDOM": 2.0,
        "ALRM_LETAR": 2.0,
        "ALRM_HEPAT": 2.0,
        "ALRM_LIQ": 2.0,
        "GRAV_PULSO": 2.0,
        "GRAV_CONV": 2.0,
        "GRAV_ENCH": 2.0,
        "GRAV_INSUF": 2.0,
        "GRAV_TAQUI": 2.0,
        "GRAV_EXTRE": 2.0,
        "GRAV_HIPOT": 2.0,
        "GRAV_HEMAT": 2.0,
        "GRAV_MELEN": 2.0,
        "GRAV_CONSC": 2.0,
        "GRAV_ORGAO": 2.0
    }

    return registro