
#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# 
import ...


class NomeClasse1:
    """descrição NomeClasse1"""

    def __init__(self, valor1, ...):
        """descrição metodo construtor"""

        pass
    
    def nomeFuncao(self):
        """descrição metodo nomeFuncao"""

        pass


class NomeClasse2:
    """descrição NomeClasse2"""

    def __init__(self):
        """descrição metodo construtor"""

        pass


def nomeFuncao(self):
    """descrição metodo nomeFuncao"""

    pass



# main só é executada quando esse módulo é o utilizado na linha de comando
# quando importado, a função main não é executada
def main():
    print("...")

    print(NomeClasse1().__doc__)

    #nomeFuncao(...)
    print(NomeClasse1.nomeFuncao.__doc__)

    #nomeFuncao(...)
    print(NomeClasse2.nomeFuncao.__doc__)


if __name__ == "__main__":
    main()
