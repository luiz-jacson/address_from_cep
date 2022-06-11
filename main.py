from cep import Cep
import requests
from os import system

def main():
    try:
        Cep(input('Digite o CEP:(Apenas números)\n'))
    except ValueError:
        system('cls')
        print('Erro! Digite um CEP válido')
        main()
    input('Pressione Enter para digitar outro CEP...')
    system('cls')
    main()



if __name__ == '__main__':
    main()


