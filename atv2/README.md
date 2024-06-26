# EML 1.2 - Do notebook para produção
API de previsão de churn 
  Esta é uma API simples construída com Flask para prever o churn de clientes usando um notebook criado
  nas disciplina iml1 que prevê o churn com base nas features:
  - is_tv_subscriber
  - is_movie_package_subscriber
  - subscription_age
  - has_contract
  O modelo de previsão é treinado usando regressão logística e está disponível para uso via solicitações HTTP.

## Pré-requisitos

Python 3.x instalado em seu sistema.
Bibliotecas Python listadas em requirements.txt instaladas.

## Instalação

Forneça instruções passo a passo sobre como instalar e configurar seu projeto. Por exemplo:

1. Clone este repositório:
    ```
    git clone https://github.com/fabiflorentin/eml1.git
    ```
2. Navegue até o diretório do projeto:
    ```
    cd atv2
    ```
3. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```

## Como Rodar localmente

1. Execute o arquivo app.py para iniciar o servidor Flask:

```
    python3 app.py
```

2. Após iniciar o servidor, a API estará disponível em http://localhost:5000/predict


## Como Usar a API

Você pode enviar solicitações GET para a rota /predict com os parâmetros tv_sub, movie_sub, age e has_contract para previsões de churn.

Por exemplo, usando o curl:
```
    curl -X GET "http://localhost:5000/predict?tv_sub=0&movie_sub=0&age=1&has_contract=0"

```

Exemplo de resposta:
```
{
  "churn": 0
}

```
Sendo que :
0 - previsão não churn
1 - previsão churn

## Gerando imagem e executando container 

1. Para gerar imagem 
```
docker build -t churn-pred .
``` 

2. Para executar o container
```
docker run -p 5000:5000 churn-pred
```

