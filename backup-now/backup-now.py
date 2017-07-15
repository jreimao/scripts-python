
#!/usr/bin/env python
# -*- encoding: utf-8 -*- 

# utilizar lista 'argv' - armazena argumnetos que entram programa python pela lnha comandos
import sys

# biblioteca python - operacoes sobre directorios/arquivos
import os, shutil



def copyDir(origem, destino):
    """ descricao metodo """
    
    # verifica se existe o directório origem
    if os.path.exists(origem):
        
        # verifica se ja existe no destino algum diretorio com o mesmo nome
        if not os.path.exists(destino):
            shutil.copytree(origem, destino)
            print('copia realizada com sucesso')

        else:
            print('não foi possível copiar o diretório, \nporque no destino já existe um com o mesmo nome')

    else:
        print('não foi possível encontrar o directório a copiar!')


def copyFile(origem, destino):
    """ descricao metodo """

    pass


def main(config):
    """ descricao metodo """

    #print(copyDir.__doc__)
    #print(copyFile.__doc__)

    origem, destino = config[1], config[2]
    
    copyDir(origem, destino)
    #copyFile(origem, destino)




breveDesc = """
script em python permite copiar um directório ou arquivo

sintaxe: python backup-now.py enderecoOrigem enderecoDestino [Enter]
exemplo - python backup-now.py c:\worktoday d:\workToday
"""
print(breveDesc)


# regista em 'config' parametros recebido da linha comandos
config = sys.argv

# define parametro obrigatorios por defeito
if len(config) < 2:
    config =[config[0], 'workToday', 'd:\workToday']


# instrução impede a execução do script quando importado!
if __name__ == '__main__':
    main(config)
