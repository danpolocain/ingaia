# inGaia-weather-music-api

Este repositório é referente ao teste e Engenheiro de Dados.

```text
Um estudo organizado por um grupo de pesquisadores desocupados demonstrou que as pessoas tendem a preferir diferentes gêneros musicais de acordo com a temperatura ambiente. 
Baseado nesta incrível descoberta, você foi contratada(o) para desenvolver um serviço revolucionário que irá sugerir músicas ao usuário de acordo com a temperatura atual da cidade dele!


Os requisitos funcionais são simples:

    Seu serviço deve ser acessível através de uma API RESTful.
    Seu serviço deve aceitar o nome de uma cidade como parâmetro, e a partir disso retornar uma playlist (somente o nome das músicas já é o suficiente) de acordoc
    com a temperatura atual na cidade fornecida.
    Se a temperatura:
    for de 25ºC ou maior, o serviço deve sugerir músicas Pop;
    estiver entre 10ºC e 25ºC, o serviço deve sugerir músicas de Rock;
    estiver abaixo de 10ºC, a sugestão deve ser de músicas clássicas;
```

#### PARADIGMA SERVERLESS:
![serverless](friends.jpg)
 
Para a entrega do teste, uma API foi criada utilizando os serviços serverless em nuvem da AWS.
Com o paradigma serverless, a aplicação fica altamente escalável, com baixo custo e principalmente sem 
o custo de manutenção de servidores. Além da API, a cada requisição os dados são gravados em um banco
de dados para serem consultado em uma camada de visualização (METABASE).

#### SERVIÇOS UTILIZADOS

- AWS API GATEWAY
    - Serviço gerenciado focado em criar APIs REST abstraindo toda a configuração de servidor. Ao receber o request no endpoint, o serviço executa o Lambda (ingaia-weather-api) para processar a resposta. [Saiba Mais](https://aws.amazon.com/pt/api-gateway/)

- AWS LAMBDA
    - Com o Lambda é possível executar códigos sem a necessidade de provisionar ou gerenciar servidores. O Lambda ingaia-weather-api é reponsável por fazer o request na api do openweathermap para receber informações sobre a cidade escolhida (Latitude, Longitude e Temperatura), após isto, ele cruza as informações com a API do Deezer para retornar uma playlist relacionada com a temperatura. Este lambda também é responsável por persistir os dados no banco de dados. [Saiba Mais](https://aws.amazon.com/pt/lambda/)
    
- AWS Elastic Beanstalk
    - Foi utilizado para provisionar o Metabase. O Beanstalk  se encarrega automaticamente da implementação, desde o provisionamento de capacidade, o balanceamento de carga e a escalabilidade automática até o monitoramento da saúde do aplicativo. 
    [Saiba Mais](https://aws.amazon.com/pt/elasticbeanstalk/)
    
- AWS RDS
    - Serviço de banco de dados gerenciado da AWS. Foi utilizado para armazenar os dados de requisição da API. [Saiba Mais](https://aws.amazon.com/pt/rds/)

- METABASE
    - Ferramenta Open Source de BI. [Saiba Mais](https://www.metabase.com/)
    
#### ACESSO API

Para acessar a API é necessário fazer o request com o método POST no seguinte endpoint:
- https://hac2l1dh5k.execute-api.us-east-1.amazonaws.com/prod/

Contendo:
- HEADERS:
    ```Authorization: AWS4-HMAC-SHA256 Credential=AKIA3ANPWIJXU7RQQHGW/20191015/us-east-1/execute-api/aws4_request, SignedHeaders=cache-control;content-length;content-type;host;postman-token;x-amz-date, Signature=942060209f95038c7b47cb0f6b6c07daa471fbac41e2a3ea96f82eb048fc2bf4```
- BODY:
    ```{ "city": "NOME DA CIDADE", "user": "ID USUÁRIO" }```

###### Obs: o parâmetro "user" foi criado apenas para simular também o registro do id de usuário na requisição.

#### ACESSO AO METABASE

Como camada de visualização uma instância do Metabase foi criada para simular um dashboards com dados da API.

Acesso: [METABASE](http://ingaia.us-east-1.elasticbeanstalk.com/


|            |           |
| ---------- |:---------:|
| LOGIN:     | ingaia    |
| SENHA:     | ingaia123 | 


Para a exploração dos dados foi criado um dashboard de exemplo (inGaia API Dash). Além do dash é possível explorar livremente os dados (Browse Data -> postgres -> inGaia Weather Music API).




###### OBS: TODOS OS SERVIÇOS UTILIZADOS NESTE TESTE ESTÃO NA FREE TIER DA AWS, PODENDO APRESENTAR INSTABILIDADE/ LENTIDÃO