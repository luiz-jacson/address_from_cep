import requests


class Cep():
    def __init__(self, cep):
        if self.valida_cep(cep):
            self.retorna_endereco(cep)

    def __str__(self):
        return '{}-{}'.format(self.cep[:5], self.cep[5:])

    def valida_cep(self,cep):
        r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if r.ok:
            return True
        else:
            return False
            print('Erro! Digite um CEP válido')

    def retorna_endereco(self, cep):
        r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        end = r.json()
        print('CEP:',end['cep'])
        print('Logradouro:',end['logradouro'])
        print('Complemento:',end['complemento'])
        print('Bairro:',end['bairro'])
        print('Cidade:',end['localidade'])
        print('Estado:',end['uf'])