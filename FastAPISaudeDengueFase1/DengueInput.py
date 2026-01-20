from pydantic import BaseModel, Field

class DengueInput(BaseModel):
    FEBRE: int = Field(..., description="Paciente apresentou febre? 1 = Sim, 2 = Não", example=1)
    MIALGIA: int = Field(..., description="Presença de mialgia (dor muscular)? 1 = Sim, 2 = Não", example=1)
    CEFALEIA: int = Field(..., description="Presença de cefaleia (dor de cabeça)? 1 = Sim, 2 = Não", example=2)
    VOMITO: int = Field(..., description="Paciente apresentou vômito? 1 = Sim, 2 = Não", example=1)
    NAUSEA: int = Field(..., description="Paciente presentation náusea? 1 = Sim, 2 = Não", example=2)
    DOR_COSTAS: int = Field(..., description="Presença de dor nas costas? 1 = Sim, 2 = Não", example=1)
    ARTRALGIA: int = Field(..., description="Presença de artralgia (dor nas articulações)? 1 = Sim, 2 = Não", example=1)
    DOR_RETRO: int = Field(..., description="Dor retro-orbitária? 1 = Sim, 2 = Não", example=2)
    RESUL_SORO: int = Field(..., description="Resultado do exame de soro - 1 = Sim, 2 = Não", example=1)
    RESUL_NS1: int = Field(..., description="Resultado do exame NS1 - 1 = Sim, 2 = Não", example=2)
    EVOLUCAO: int = Field(..., description="Evolução do caso do paciente - 1 = Sim, 2 = Não", example=1)

    ALRM_HIPOT: int = Field(..., description="Sinal de alarme: hipotensão - 1 = Sim, 2 = Não", example=2)
    ALRM_PLAQ: int = Field(..., description="Sinal de alarme: queda de plaquetas - 1 = Sim, 2 = Não", example=1)
    ALRM_VOM: int = Field(..., description="Sinal de alarme: vômitos persistentes - 1 = Sim, 2 = Não", example=2)
    ALRM_SANG: int = Field(..., description="Sinal de alarme: sangramento - 1 = Sim, 2 = Não", example=2)
    ALRM_HEMAT: int = Field(..., description="Sinal de alarme: alteração hematológica - 1 = Sim, 2 = Não", example=2)
    ALRM_ABDOM: int = Field(..., description="Sinal de alarme: dor abdominal intensa - 1 = Sim, 2 = Não", example=2)
    ALRM_LETAR: int = Field(..., description="Sinal de alarme: letargia - 1 = Sim, 2 = Não", example=2)
    ALRM_HEPAT: int = Field(..., description="Sinal de alarme: aumento do fígado - 1 = Sim, 2 = Não", example=2)
    ALRM_LIQ: int = Field(..., description="Sinal de alarme: acúmulo de líquidos - 1 = Sim, 2 = Não", example=2)

    GRAV_PULSO: int = Field(..., description="Sinal de gravidade: pulso fraco - 1 = Sim, 2 = Não", example=2)
    GRAV_CONV: int = Field(..., description="Sinal de gravidade: convulsões - 1 = Sim, 2 = Não", example=2)
    GRAV_ENCH: int = Field(..., description="Sinal de gravidade: enchimento capilar alterado - 1 = Sim, 2 = Não", example=2)
    GRAV_INSUF: int = Field(..., description="Sinal de gravidade: insuficiência respiratória - 1 = Sim, 2 = Não", example=2)
    GRAV_TAQUI: int = Field(..., description="Sinal de gravidade: taquicardia - 1 = Sim, 2 = Não", example=2)
    GRAV_EXTRE: int = Field(..., description="Sinal de gravidade: extremidades frias - 1 = Sim, 2 = Não", example=2)
    GRAV_HIPOT: int = Field(..., description="Sinal de gravidade: hipotensão grave - 1 = Sim, 2 = Não", example=2)
    GRAV_HEMAT: int = Field(..., description="Sinal de gravidade: alteração grave hematológica - 1 = Sim, 2 = Não", example=2)
    GRAV_MELEN: int = Field(..., description="Sinal de gravidade: presença de melena - 1 = Sim, 2 = Não", example=2)
    GRAV_CONSC: int = Field(..., description="Sinal de gravidade: alteração do nível de consciência - 1 = Sim, 2 = Não", example=2)
    GRAV_ORGAO: int = Field(..., description="Sinal de gravidade: comprometimento de órgão - 1 = Sim, 2 = Não", example=2)

    class Config:
        schema_extra = {
            "example": {
                "FEBRE": 1,
                "MIALGIA": 1,
                "CEFALEIA": 2,
                "VOMITO": 1,
                "NAUSEA": 2,
                "DOR_COSTAS": 1,
                "ARTRALGIA": 1,
                "DOR_RETRO": 2,
                "RESUL_SORO": 1,
                "RESUL_NS1": 2,
                "EVOLUCAO": 1,
                "ALRM_HIPOT": 2,
                "ALRM_PLAQ": 1,
                "ALRM_VOM": 2,
                "ALRM_SANG": 2,
                "ALRM_HEMAT": 2,
                "ALRM_ABDOM": 2,
                "ALRM_LETAR": 2,
                "ALRM_HEPAT": 2,
                "ALRM_LIQ": 2,
                "GRAV_PULSO": 2,
                "GRAV_CONV": 2,
                "GRAV_ENCH": 2,
                "GRAV_INSUF": 2,
                "GRAV_TAQUI": 2,
                "GRAV_EXTRE": 2,
                "GRAV_HIPOT": 2,
                "GRAV_HEMAT": 2,
                "GRAV_MELEN": 2,
                "GRAV_CONSC": 2,
                "GRAV_ORGAO": 2
            }
        }
