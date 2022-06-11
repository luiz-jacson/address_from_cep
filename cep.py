import requests


class Cep():
    def __init__(self, cep):
        self._cep = cep
        if self.valida_cep(self._cep):
            self.retorna_endereco(cep)

    def __str__(self):
        return self._cep

    def valida_cep(self,cep):
        r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if r.ok:
            return True
        else:
            raise ValueError

    def retorna_endereco(self, cep):
        r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        end = r.json()
        print('CEP:',end['cep'])
        print('Logradouro:',end['logradouro'])
        print('Complemento:',end['complemento'])
        print('Bairro:',end['bairro'])
        print('Cidade:',end['localidade'])
        print('Estado:',end['uf'])