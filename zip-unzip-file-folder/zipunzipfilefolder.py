
#!/usr/bin/env python
# -*- encoding: utf-8 -*- 


# modulo zipfile permite extrair|comprimir arquivo(s)|directoria(s) em python
import zipfile

# modulo os e as suas funções permite interagir com o sistema operacional
import os

# modulo glob com a função 'glob' que permite fazer listas de arquivo(s)|sub-directorio(s) de um diretório
import glob



class zipunzip:
    """
class in python that allows to compress|extract file(s)|directory(ies)

consult:
dir(zipunzipfilefolder.zipunzip) [Enter]
print(zipunzipfilefolder.zipunzip.nameMethod.__doc__) [Enter]
    """



    def __init__(self):
        """ method constructor """



    def zipfile(data):
        """
zipfile(data) : method compresses a specific file

syntax:
data = ['fullPathFile', 'fullPathFileZip']
zipunzipfilefolder.zipunzip.zipfile(data)
        """

        if len(data) < 2:
                
            print("nr argumentos insuficiente!")

        else:
            
            # distribuir os argumentos por variaveis
            origem, destino = data[0], data[1]

            folder_file_origem = os.path.split(origem)
            # ('C:\\...\\...\\zip-unzip-file-folder', 'tutorial.pdf')
            # folder_file_origem[0] or folder_file_origem[1]

            folder_file_destino = os.path.split(destino)
            # ('C:\\...\\...\\zip_python', 'archive.zip')

            
            # avalia origem é um arquivo
            if os.path.isfile(origem):


                # cria o arquivo zip na mesma pasta do arquivo original
                file = zipfile.ZipFile(folder_file_destino[1], 'w')

                # guarda o endereco completo arquivo zipado
                # origem: 'C:\\...\\...\\tutorial.pdf' != 'tutorial.pdf'
                # compress_type = zipfile.ZIP_DEFLATED | compress_type = zipfile.ZIP_BZIP2 | 
                # | compress_type = zipfile.ZIP_LZMA
                file.write(origem, compress_type = zipfile.ZIP_DEFLATED)
                
                # nao guarda o endereco completo arquivo zipado
                #file.write(origem, folder_file_origem[1], compress_type = zipfile.ZIP_DEFLATED)


                # fecha arquivo zip
                file.close()
                print("arquivo comprimido com sucesso")


            else:
                print('não foi encontrado o arquivo para zipar')



    def unzipfile(data):
        """
unzipfile(data) : method extracts a specific file

syntax:
data = ['fullPathFileZip', 'pathFolderDestiny', 'nameFile']
zipunzipfilefolder.zipunzip.unzipfile(data)
        """

        if len(data) < 3:
                
            print("nr argumentos insuficiente!")

        else:

            # atribui a cada variavel, um item da lista dados recebida pela função
            origem, destino, arquivo = data[0], data[1], data[2]

            # sequencias de if que avaliam zip da origem e pasta destino
            if os.path.isfile(origem):
        

                zip = os.path.splitext(origem)
                if zip[1] == '.zip':
                    

                    if os.path.isdir(destino):
                        
                        file = zipfile.ZipFile(origem)
                        file.extract(arquivo, destino)
                        file.close()

                        print("arquivo extraido com sucesso")

                    else:
                        print("não indicou uma directoria destino valida para extração!")

                
                else:
                    print("o arquivo indicado não é tipo zip!")


            else:
                print("não foi encontrado o arquivo para extrair!")



    def zipfilesdir(data):
        """
zipfilesdir(data) : method compresses all files or a file with a specific extension 
                    in a folder (does not include subfolders)

syntax:
data = ['pathFolderSearch', '*.*'|'*.extension'|'fileName.extension', 'fullPathFileZip']
zipunzipfilefolder.zipunzip.zipfilesdir(data)
        """

        if len(data) < 3:
                
            print("nr argumentos insuficiente!")

        else:

            # atribui a cada variavel, um item da lista dados recebida pela função
            origem, tipoficheiro, destino = data[0], data[1], data[2]
            
            # une endreço completo directório e a extensão a procurar 
            oriExt = os.path.join(origem, tipoficheiro)


            # sequencias de if que avaliam zip da origem e pasta destino
            if os.path.isdir(origem):


                zip = os.path.splitext(destino)
                if zip[1] == '.zip':
                    
                        
                    # filesDir : lista com nomeArquivos encontrados
                    # glob.glob(oriExt) : procura arquivo(s) com determinada(s) extenso(oes)
                    # mas apenas na directoria defenida
                    filesDir = glob.glob(oriExt) # '*.txt' or ...

                    # se não encontrar arquivo(s), não criar arquivo zip
                    if len(filesDir) > 0:
                        
                        # criar arquivo zip destino
                        file = zipfile.ZipFile(destino, 'w')
                        
                        # iteração pelo(s) arquivo(s) encontrados
                        for fileDir in filesDir:     

                            # guarda apenas nome do(s) arquivo(s)
                            #file.write(fileDir, compress_type = zipfile.ZIP_DEFLATED)

                            # guarda endereço completo do(s) arquivo(s)
                            # os.path.abspath(nomeArquivo) : retorna endereço completo arquivo
                            filePath = os.path.abspath(fileDir)
                            # adiciona o(s) arquivo(s) encontrados ao zip
                            file.write(filePath, compress_type = zipfile.ZIP_DEFLATED)

                        # fecha arquivo zip
                        file.close()

                        print("arquivo(s) comprimido(s) com sucesso")


                    else:
                        print("não foi encontrado o tipo arquivo pedido!")

                
                else:
                    print("o arquivo indicado não é tipo zip!")


            else:
                print("não indicou uma directoria valida para procurar arquivos!")



    def zipfilesdirs(data):
        """
zipfilesdirs(data) : method compresses all files or a specific file in a folder (including 
                     subfolders)

syntax:
data = ['pathFolderSearch', ''|'.extension', 'fullPathFileZip']
zipunzipfilefolder.zipunzip.zipfilesdirs(data)
        """

        if len(data) < 3:
                
            print("nr argumentos insuficiente!")

        else:

            # atribui a cada variavel, um item da lista dados recebida pela função
            origem, tipoficheiro, destino = data[0], data[1], data[2]



            # sequencias de if que avaliam zip da origem e pasta destino
            if os.path.isdir(origem):


                # une endreço completo directório e a extensão a procurar 
                oriExt = os.path.join(origem, tipoficheiro)

                zip = os.path.splitext(destino)
                if zip[1] == '.zip':

                    
                    fileszip = zipfile.ZipFile(destino, 'w')

                    for folder, subfolders, files in os.walk(origem):
                    
                        # a cada arquivo (file) de um conjunto de 'files' ira:
                        for file in files:
                            
                            # sem especificar tipoficheiro
                            if not tipoficheiro:

                                # salva endereco completo do(s) arquivo(s) zipado(s)
                                fileszip.write(os.path.join(folder, file), compress_type = zipfile.ZIP_DEFLATED)


                            # tipoficheiro especificado
                            else:
                                
                                # especificar tipo de ficheiro a zipar - '.txt' ou '.pdf' ou ...
                                if file.endswith(tipoficheiro):

                                    # salva endereco completo do(s) arquivo(s) zipado(s)
                                    fileszip.write(os.path.join(folder, file), compress_type = zipfile.ZIP_DEFLATED)

                    fileszip.close()

                    print("arquivo(s) comprimido(s) com sucesso")

                    
                else:
                    print("o arquivo indicado não é tipo zip!")


            else:
                print("não indicou uma directoria valida para procurar arquivos!")



    def unzipfiles(data):
        """
unzipfiles(data) : method extracts all files from a zip

syntax:
data = ['fullPathFileZip', 'pathFolderDestiny']
zipunzipfilefolder.zipunzip.unzipfiles(data)
        """

        if len(data) < 2:
            
            print("nr argumentos insuficiente!")

        else:
            
            # atribui a cada variavel, um item da lista dados recebida pela função
            origem, destino = data[0], data[1]

            # sequencias de if que avaliam zip da origem e pasta destino
            if os.path.isfile(origem):
        
                zip = os.path.splitext(origem)
                if zip[1] == '.zip':
                    
                    if os.path.isdir(destino):
                        
                        
                        fileszip = zipfile.ZipFile(origem)
                        fileszip.extractall(destino)
                        fileszip.close()


                    else:
                        print("não indicou a directoria destino para extração!")

                else:
                    print("o arquivo indicado não é tipo zip!")

            else:
                print("não indicou o arquivo zip para a extração!")



    def unzipfiledirs(data):
        """
unzipfiledirs(data) : method extracts a specific file from a zip (including subfolders)

syntax:
data = ['fullPathFileZip']
zipunzipfilefolder.zipunzip.unzipfiledirs(data)  =>  listFiles of fullPathFileZip

data = ['fullPathFileZip', 'pathFolderDestiny', 'nameFile']
zipunzipfilefolder.zipunzip.unzipfiledirs(data)  =>  extract 'nameFile' of fullPathFileZip
        """

        # conjunto if avaliam o nr e tipo de argumento(s)
        if len(data) == 0:
            
            print("nr argumentos insuficiente!")


        # perante os argumento(s) avalia se lista ou extrai arquivos
        else:
            
            # avalia se origem é do tipo arquivo
            origem = data[0]
            if os.path.isfile(origem):
                
                # avalia se origem é do tipo zip
                zip = os.path.splitext(origem)
                if zip[1] == '.zip':


                    # nr argumento >= 3 - extarair arquivos
                    if len(data) >= 3:
                        

                        # distribui por variaveis alguns argumentos
                        destino, nomeArquivo = data[1], data[2]

                        # avalia se destino é do tipo directoria
                        if os.path.isdir(destino):
                            

                            # variavel indica se encontrou/extraiu arquivo(s) procurado(s) 
                            extractFile = False

                            # abre arquivo zip
                            filezip = zipfile.ZipFile(origem)

                            # ciclo for que procura arquivo(s) dentro do zip
                            for file in filezip.namelist():
                            
                                # compara nome do(s) arquivos do zip com o(s) procurado(s)
                                if (str(os.path.basename(file)) == nomeArquivo):                                
                                
                                    # extrai arquivo
                                    filezip.extract(file, destino)
                                    # variavel passa a True porque foi encontrado pelo menos um arquivo
                                    extractFile = True

                            if extractFile:
                                print("arquivo(s) extraido(S) com sucesso")
                            else:
                                print("não foi encontrado o arquivo pedido!")

                            # fecha arquivo zip
                            filezip.close()
                            

                        else:
                            print("erro da indicação da directoria destino!")


                    # nr argumento < 3 - imprimir listagem arquivos do zip
                    else:
                        
                        # lista ira conter arquivos encontrados dentro zip
                        listfile = []

                        filezip = zipfile.ZipFile(origem)

                        for file in filezip.namelist():
                            # acrescenta todos os arquivos encontrados (zip) a lista 'listfile'
                            listfile.append(os.path.basename(file))
                        
                        # imprime a lista do nome dos arquivos contidos no zip
                        print(listfile)

                        # fecha arquivo zip
                        filezip.close()


                else:
                    print("não indicou o arquivo zip para listar!")
            
            else:
                print("endereço arquivo inválido!")  



# main só é executada quando esse módulo é o utilizado na linha de comando
# quando importado, a função main não é executada
def main():
    
    print(zipunzip().__doc__)

        #print(zipunzipfilefolder.zipunzip.nomeMetodo.__doc__)

    #zipfile(data)
    #print(zipunzip.zipfile.__doc__)

    #unzipfile(data)
    #print(zipunzip.unzipfile.__doc__)

    #zipfilesdir(data)
    #print(zipunzip.zipfilesdir.__doc__)

    #zipfilesdirs(data)
    #print(zipunzip.zipfilesdirs.__doc__)

    #unzipfiles(data)
    #print(zipunzip.unzipfiles.__doc__)

    #unzipfiledirs(data)
    #print(zipunzip.unzipfiledirs.__doc__)



if __name__ == '__main__':
    main()
