#from select import select

comando = "SELECT dept_no, dept_name, first_name FROM departments, employees_copy WHERE from_date > 2000 AND to_date < 1000 ORDER BY empt_no ;".replace(',', ' ').replace(';', '').rstrip(',').casefold().split()
#input("Qual o comando SQL?").replace(',', ' ').replace(';', '').rstrip(',').casefold().split()

# Computando os índices em que se encontram os comandos na lista
ind_select = comando.index('select')
ind_from = comando.index('from')
tam_comando = len(comando)
# Computando os índices não opcionais com exceções caso eles não existam
try:
    ind_order = comando.index('order')
except:
    ind_order = tam_comando
try:
    ind_where = comando.index('where')
except:
    ind_where = ind_order

# Separando por partes do comando conforme lógicas criadas
com_select = comando[ind_select+1:ind_from]
com_from = comando[ind_from+1:ind_where]
com_where = comando[ind_where+1:ind_order]
com_order = comando[ind_order+2:tam_comando]

def printarComando():
    print(comando)
    print("")

def executarComando(ListaTabelasNome, ListaTabelas, QtdeAtributos):
    # Gera tabela com todos os dados contidos em FROM
    Query = fromTudo(ListaTabelasNome, ListaTabelas)
    # Gera tabela com as colunas especificadas em SELECT
    Query = select(Query)
    # Imprime a Query final
    print(*Query, sep = '\n')


def select(Query):
    if (com_select[0] == "*"):
        return Query
    else:
        # Criada nova Query
        NovaQuery = []

        lenSel = len(com_select)

        i = Query[0].index(com_select[0])
        for q in range(len(Query)):
            NovaQuery.append([Query[q][i]])

        if (lenSel > 1):
            # Busca o índice de um atributo nas colunas
            for atributo in com_select[1:lenSel]:
                i = Query[0].index(atributo)

                for q in range(len(Query)):
                    NovaQuery[q].append(Query[q][i]) 

        return NovaQuery

def fromTudo(ListaTabelasNome, ListaTabelas):
    # Flag se mantém em 1 caso haja apenas um parâmetro
    lenCom = len(com_from)

    nome_tabela = com_from[0]
    i = ListaTabelasNome.index(nome_tabela)
    Tabela = ListaTabelas[i]

    if lenCom > 1:
        Query = Tabela
        for nome_tabela in com_from[1:lenCom]:
            # Busca o índice de um atributo para achar a(s) tabela(s) correspondente(s)
            i = ListaTabelasNome.index(nome_tabela)
            Tabela = ListaTabelas[i]
            
            # Cópia feita para manipular e depois esvaziar a query
            QueryAnterior = Query.copy()
            Query = [[]]

            # Apenas o cabeçalho é copiado uma única vez
            for atributos in QueryAnterior[0]:
                Query[0].append(atributos)
            for atributos in Tabela[0]:
                Query[0].append(atributos)

            # Contador para as linhas da nova tabela
            cont = 1

            # Para cada linha de uma tabela, a outra tabela gerará todas as suas linhas
            for q in range (1, len(QueryAnterior)):
                for t in range(1, len(Tabela)):
                    Query.append(QueryAnterior[q].copy())
                    for atributo in Tabela[t]:
                        Query[cont].append(atributo)
                    cont = cont + 1

    return Query
