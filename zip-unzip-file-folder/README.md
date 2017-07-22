
###### [read this page in english](https://github.com/jreimao/scripts-python/blob/zip-unzip-file-folder/zip-unzip-file-folder/README-en.md)

# [script-python](https://github.com/jreimao/scripts-python/tree/master)


### sobre zip-unzip-file-folder

> classe em Python que permite comprimir ou extrair ficheiro(s) e pasta(s)

  **_mais detalhes_**:
  dir(zipunzipfilefolder.zipunzip) [Enter]
  print(zipunzipfilefolder.zipunzip.nameMethod.\__doc__) [Enter]

  **_metódos disponíveis na classe_**:
  1. **zipfile(data)** : metódo comprime um arquivo específico
  2. **unzipfile(data)** : metódo extrai um arquivo específico
  3. **zipfilesdir(data)** : metódo comprime todos os arquivos ou arquivos com uma determinada extensão de uma pasta (não inclui as possiveis sub-pastas)
  4. **zipfilesdirs(data)** : metódo comprime todos os arquivos ou arquivos com uma determinada extensão de uma pasta (inclui todas as possiveis sub-pastas)
  5. **unzipfiles(data)** : metódo extrai todos arquivos de um zip
  6. **unzipfiledirs(data)** : metódo extrai todos arquivos de um zip (inclui todas as possiveis sub-pastas)


### requisitos e execução
##### requisitos
  \- python 3.6 (https://www.python.org/downloads/ )

##### executar script
linha de comandos (windows):

_zipfilesdirs(data)
syntax:
data = ['pathFolderSearch', ''|'.extension', 'fullPathFileZip']
zipunzipfilefolder.zipunzip.zipfilesdirs(data)_

```sh
...@... C:\...\scripts-python\zip-unzip-file-folder
> python
Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import zipunzipfilefolder
>>>
>>> data = ['C:\\...\\criarExtrairArquivoZip', '.txt', 'C:\\...\\Desktop\\zipPython.zip']
>>>
>>> zipunzipfilefolder.zipunzip.zipfilesdirs(data)
arquivo(s) comprimido(s) com sucesso
>>> |
```

### licença
MIT
**aplicação gratuita**


### autor
![foto joão reimão](https://avatars2.githubusercontent.com/u/15116081?v=3&s=75 "joão reimão")
joão reimão | web and mobile programmer | email: jreimao@yahoo.com
