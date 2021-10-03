# osint_python

Tratamento de dados vindos do Spiderfoot

## Indice

<!--ts-->

1. [Sobre](##Sobre)
2. [Pré requisitos](##Pré-Requisitos)
3. [Instalação](##Instalação)
   1. [Postgres](###Postgres)

<!--te-->

## Sobre

Uma interface para analise de grandes volumes de dados em series temporais usando a ferramenta [Spiderfoot](https://github.com/smicallef/spiderfoot)

## Pré requisitos

Pata utilizar a cli é necessário ter instalado o Python 3, caso queira persistir os dados em um banco de dados postgres é necessário um servidor com ele instalado.

Na parte de [configuração](#Configuração) estão os detalhes do banco de dados.

## Instalação

O unico comando necessário para instalar as dependencias é

```
pip install -r requirements.txt
```

Caso queira usar um ambiente virtual para instalar os pacotes do python basta fazer

```
python -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

### Postgres

Para usar um banco de dados postgres externo basta colocar os dados nas variáveis de ambiente.

Pode ser direto no PATH do sistema operacional ou preenchenco o arquivo .env usando de exemplo o arquivo .env.example.

Então é só usar s flag --postgres nos comando que aceitam.
