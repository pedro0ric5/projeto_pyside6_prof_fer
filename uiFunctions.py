import requests
import json

def consulta_cnpj(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "plugin":"RF"}
    response = requests.get(url, params=querystring)

    resp = json.loads(response.text)

    campos = (
        resp['nome'],
        resp['logradouro'],
        resp['numero'],
        resp['complemento'],
        resp['bairro'],
        resp['municipio'],
        resp['uf'],
        resp['cep'],
        resp['telefone'],
        resp['email'],
    )

    return campos

#consulta_cnpj('07591060000175')