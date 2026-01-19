# 8IADT-tech-challenge-fase1
8IADT - Tech Challenge Fase 1 - Machine Learning - Saude Dengue

Rodrigo Oliveira de Andrade - rm369879

Felipe Villa do Conde - rm369942


# API de Predição de Dengue

Projeto de API desenvolvida em Python usando FastAPI para realizar predições
de hospitalizações de casos de dengue com base em dados clínicos informados, sendo uma ferramenta para ajuadar a equipe médica a decidir casos de hospitalizações.

## Tecnologias utilizadas

- Python 3.12
- FastAPI
- Scikit-learn  1.6.1
- Pandas
- Docker

## Como instalar

### 1. Criar ambiente virtual

python3 -m venv ./venv

ou

python -m venv .venv

source .venv/bin/activate

### 2. Instalar dependências

pip install scikit-learn==1.6.1

pip install pandas

pip install -r requirements.txt

### 3. Atualização de versão

pip install --upgrade pip

## Como executar localmente

fastapi dev main.py

Endpoint: http://127.0.0.1:8000/docs

## Como executar com Docker

docker build -t api-dengue .

docker run -p 8001:8001 api-dengue


Ubuntu

sudo docker run -p 8001:8001 api-dengue

Endpoint: http://127.0.0.1:8001/docs

### 4.Endpoints

POST /predict  

Recebe um JSON com sintomas e retorna a predição.

Exemplo payload de requisição:

Dados válidos: 1.0 (Sim)  / 2.0 (Não)

```
{
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
```

# Projeto

O dataset e o dicionário de dados foram obtidos através do site do Ministério da Saúde: https://dadosabertos.saude.gov.br/dataset/arboviroses-dengue

Dataset - Dengue 2025:


Dicionario de dados:








