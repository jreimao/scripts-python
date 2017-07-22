
###### [leia esta página em português](https://github.com/jreimao/scripts-python/tree/zip-unzip-file-folder/zip-unzip-file-folder)

# [script-python](https://github.com/jreimao/scripts-python/blob/master/README-en.md)


### about zip-unzip-file-folder

> class in python that allows to compress or extract file(s) and directory(ies)

  **_more details_**:
  dir(zipunzipfilefolder.zipunzip) [Enter]
  print(zipunzipfilefolder.zipunzip.nameMethod.\__doc__) [Enter]

  **_available methods in class_**:
  1. **zipfile(data)** : method compresses a specific file
  2. **unzipfile(data)** : method extracts a specific file
  3. **zipfilesdir(data)** : method compresses all files or a file with a specific extension in a folder (does not include subfolders)
  4. **zipfilesdirs(data)** : method compresses all files or a specific file in a folder (including subfolders)
  5. **unzipfiles(data)** : method extracts all files from a zip
  6. **unzipfiledirs(data)** : method extracts a specific file from a zip (including subfolders)


### requirements and execution
##### requisites
  \- python 3.6 (https://www.python.org/downloads/ )

##### script run
prompt commands (windows):

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

### license
MIT
**free application**


### author
![foto joão reimão](https://avatars2.githubusercontent.com/u/15116081?v=3&s=75 "joão reimão")
joão reimão | web and mobile programmer | email: jreimao@yahoo.com
