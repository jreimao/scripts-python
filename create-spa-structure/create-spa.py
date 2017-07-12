
#!/usr/bin/env python
# -*- encoding: utf-8 -*- 


# utilizar lista 'argv' - armazena argumnetos que entram programa python pela lnha comandos
import sys

# permite trabalhar com pastas e ficheiros
import os



def preparacao(args):
    """
    método coordena as tarefas de criação de pastas e ficheiros
    """

    task_folders = 1
    task_files = 1
    
    nameProject = args[1]
    folderProject = "\%s" % (nameProject)

    # verifica se já existe o directório
    if not os.path.exists(os.getcwd()+folderProject):
       diretorios(nameProject)

    else:
        task_files = 0

        # os.getcwd() : indica endereco actual
        print("a pasta "+nameProject+" já existe em "+os.getcwd())

    if task_files:
        ficheiros(nameProject)

        print("\ncriada com sucesso a estrutura da " + nameProject + " em\n" + os.getcwd())



def diretorios(nameProject):
    """
    método cria as pastas da estrutura inicial da spa
    """

    listFolders = [nameProject, nameProject+'/css', nameProject+'/images', \
                   nameProject+'/images/assets/', nameProject+'/js']

    print('pastas criadas:')
    task1 = 0
    task2 = len(listFolders)

    for folder in listFolders:
        
        os.mkdir(folder)

        task1 += 1
        # imprime as tarefas já executas
        print(str(task1)+'/'+str(task2)+' - '+str(folder))

    task_folders = 0
    print(' ')



def ficheiros(nameProject):
    """
    método cria os arquivos e os respectivos conteuúdos
    """

    html = """
<!DOCTYPE html>
<html lang="pt">
    <head>
        <!-- importar icones e fontes Google: cdn e local --> 
        <link href="http://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

        <!-- importar materialize css: cdn e local --> 
        <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/css/materialize.min.css" rel="stylesheet" />


        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">

        <meta name="description" content="peque descricao">
        <meta name="keywords" content="palavras chave">
        <meta name="author" content="nome autor">
        
        <title>%s</title>

        <link rel="icon" href="images/assets/favicon.png" type="image/x-icon">
        <link rel="stylesheet" type="text/css" href="css/style.css">

        <script src="js/index.js"></script>
    </head>
    <body>
    

        <!-- importar jQuery antes materialize.js: cdn e local --> 
        <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>

        <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/js/materialize.min.js"> </script>

    </body>
</html>
          """ % (nameProject)

    css = """ /* css */ """
    
    # imagem 32x32 ou 16x16 pixeis
    ico = ""

    js = """ /* javascript */ """

    dataFile = [html, css, ico, js]

    listFiles = {nameProject+'/': 'index.html', nameProject+'/css/': 'style.css', \
                 nameProject+'/images/assets/': 'favicon.png', nameProject+'/js/': 'index.js'}

    print('ficheiros criados:')
    task1 = 0
    task2 = len(listFiles)

    # ciclo cria os arquivos (listFiles) com os respectivos conteúdos (dataFile)
    for key in listFiles:
                    
        f = open(key+listFiles[key], 'w')
        f.write(dataFile[task1])
        f.close()

        task1 += 1
        # imprime as tarefas já executas
        print(str(task1)+'/'+str(task2)+' - '+str(key+listFiles[key]))

    task_files = 0



def main(args):
    descricao = """
script em Python que cria a estrutura inicial de uma 'Single Page 
Aplication' em HTML5, CSS (com Materialize CSS - CDN) e JavaScript

sintaxe: python createspa.py nomeProjecto [Enter]
por defeito o nome projecto é 'spa'
                """
    # imprime pequeno resumo sobre o script
    print(descricao) 
    preparacao(args)



# define lista args, permitindo executar script duplo-clique
args = ["", "spa"]

# args: lista recebe argumento(s) da linha de comando
args = sys.argv
# define o nome do projecto por defeito - spa
if len(args)<2:
    args = [args[0], "spa"]



# instrução impede a execução do script quando importado!
if __name__ == '__main__':
    main(args)
