# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/asfelix/eventex.svg?branch=master)](https://travis-ci.org/asfelix/eventex)
[![CodeFactor](https://www.codefactor.io/repository/github/asfelix/eventex/badge)](https://www.codefactor.io/repository/github/asfelix/eventex)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.8
3. Ative o seu virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:asfelix/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample.env .env
python manage.py test
```

## Como fazer o deploy

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY para a instância
4. Defina DEBUG=False
5. Configure o serviço de e-mail.
6. Envie o código para o Heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set
SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configura o e-mail
git push heroku master --force
```