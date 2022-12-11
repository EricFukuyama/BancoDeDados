import Auxiliares

comando = "SELECT * FROM dept_emp_Copia, departments where dept_emp_Copia.dept_no=departments.dept_no;".replace(',', ' ').replace(';', '').replace('\'', ' ').replace('\"', ' ').replace('(', ' ').rstrip(',').casefold().split()
#comando = input("Qual o comando SQL? ").replace(',', ' ').replace(';', '').replace('\'', ' ').replace('\"', ' ').rstrip(',').casefold().replace('inner', ' ').split()

print(comando)

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
try:
    ind_join = comando.index('join')
except:
    ind_join = ind_where
try:
    ind_using = comando.index('using')
except:
    ind_using = ind_where
try:
    ind_on = comando.index('on')
except:
    ind_on = ind_where

# Separando por partes do comando conforme lógicas criadas
com_select = comando[ind_select+1:ind_from]
com_from = comando[ind_from+1:ind_join]

if (ind_using != ind_where):
    com_join = comando[ind_join+1:ind_using]
elif (ind_on != ind_where):
    com_join = comando[ind_join+1:ind_on]
com_using = comando[ind_using+1:ind_where]
com_on = comando[ind_on+1:ind_where]

com_where = comando[ind_where+1:ind_order]
com_order = comando[ind_order+2:tam_comando]

def printarComando():
    print(comando)
    print("")

#Chama as funcoes para fazer o select, from, where e orderby
def executarComando(ListaTabelasNome, ListaTabelas):
    # Gera tabela com todos os dados contidos em FROM
    Query = fromTudo(ListaTabelasNome, ListaTabelas)
    
    try:
        if (len(com_on) != 0):
            Query = joinOn(Query, ListaTabelasNome, ListaTabelas)
        elif (len(com_using) != 0):
            Query = joinUsing(Query, ListaTabelasNome, ListaTabelas)
    except:
        i = -1

    if (len(com_where) != 0):
        #Gera tabela com os elementos que satisfazem o where
        if (Auxiliares.detectaJoin(com_where)):
            Query = joinWhere(Query)
        else:
            Query = where(Query)
    
    if (len(com_order) != 0):
        # Gera tabela devidamente ordenada com o algoritmo MergeSort
        Query = orderBy(Query)

    # Gera tabela com as colunas especificadas em SELECT
    Query = select(Query)

    # Imprime a Query final
    print(*Query, sep = '\n')


def select(Query):
    if (com_select[0] == "*"):
        return Query
    else:
        # Criada nova Query e computado tamanho
        NovaQuery = []
        lenSel = len(com_select)

        # Computada a coluna selecionada e inserida na nova Query
        i = Query[0].index(com_select[0])
        for q in range(len(Query)):
            NovaQuery.append([Query[q][i]])
    
        # Caso haja outras colunas selecionadas
        if (lenSel > 1):
            # Busca o índice de um atributo nas colunas
            for atributo in com_select[1:lenSel]:
                i = Query[0].index(atributo)
                #Inserida a informação na posição da Query
                for q in range(len(Query)):
                    NovaQuery[q].append(Query[q][i]) 

        return NovaQuery

def fromTudo(ListaTabelasNome, ListaTabelas):
    
    # Computados os valores do tamanho da tabela e do índice referente ao nome selecionado
    lenCom = len(com_from)
    nome_tabela = com_from[0]
    i = ListaTabelasNome.index(nome_tabela)

    # Simplesmente é copiada a tabela conforme o índice presente na lista de tabelas
    Tabela = ListaTabelas[i]

    # Caso tiverem mais argumentos no From
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

    # Retornada a Tabela caso o contrário
    return Tabela

def orderBy(Query):

    # Computa valores úteis que serão usados depois
    lenTabela = len(Query)
    nome_atributo = com_order[0]

    # Computa posição da coluna
    i = Query[0].index(nome_atributo)
    
    # Retirada temporariamente a primeira linha para fazer o Merge Sort
    atributos = Query[0]
    Query.pop(0)

    Auxiliares.mergeSort(Query, i)

    # Caso tenha colocado em ordem decrescente, é invertido a ordem dos elementos
    try:
        if (com_order[1] == "desc"):
            Query.reverse()
    except:
        i = -1

    # Após ordenado, é inserida novamente
    Query.insert(0, atributos)

    return Query

def where(Query):

    novaQuery=[]
    novaQuery.append(Query[0])
    comando = com_where
    #transforma em string
    comando = " ".join(com_where).casefold()
    
    #vai ter ou 1 campo(caso em que não há or ou and) ou tres campos(a primeira comparacao, a segunda e se é or ou and)
    condicao=[]

    #verifica se há comando AND
    if(comando.find(" and ")>0):
        comando = comando.split(" and ")
        condicao.append(Auxiliares.procuraWhere(comando[0]))
        condicao.append(Auxiliares.procuraWhere(comando[1]))
        condicao.append("and")

    #verifica se há comando OR
    elif(comando.find(" or ")>0):
        comando = comando.split("or")
        condicao.append(Auxiliares.procuraWhere(comando[0]))
        condicao.append(Auxiliares.procuraWhere(comando[1]))
        condicao.append("or")

    #Caso não tenha and e or
    else:
        condicao.append(Auxiliares.procuraWhere(comando))    
        
    #salvar o indice onde aparece o nome da coluna da tabela que será usado
    #caso não seja um nome de coluna, indice = -1    
    try:
        indice = Query[0].index(condicao[0][0])
    except: 
        indice =-1
    try:
        indice2=Query[0].index(condicao[0][1])
    except:
        indice2 =-1
        
    #no caso de nao ter and ou or
    if(len(condicao)==1):
        for i in range(1,len(Query)):
            if(Auxiliares.comparacao(condicao[0], indice, indice2, Query, i)):
                novaQuery.append(Query[i])
    
    #se tiver and ou or
    elif(len(condicao)==3):
        try:
            indice3 = Query[0].index(condicao[1][0])
        except: 
            indice3 =-1
        try:
            indice4=Query[0].index(condicao[1][1])
        except:
            indice4 =-1
        
        if condicao[2]=='and':
            for i in range(1,len(Query)):
                if(Auxiliares.comparacao(condicao[0], indice, indice2, Query, i) and Auxiliares.comparacao(condicao[1], indice3, indice4, Query, i)):
                    novaQuery.append(Query[i])
        
        if condicao[2]=='or':
            for i in range(1,len(Query)):
                if(Auxiliares.comparacao(condicao[0], indice, indice2, Query, i) or Auxiliares.comparacao(condicao[1], indice3, indice4, Query, i)):
                    novaQuery.append(Query[i])
        
    return(novaQuery)

def join(Query, Tabela, col1, col2, flag = 1):

    QueryJoin = [[]]

    # Apenas o cabeçalho é copiado uma única vez
    for atributos in Query[0]:
        QueryJoin[0].append(atributos)
    if flag == 1:
        for atributos in Tabela[0]:
            QueryJoin[0].append(atributos)

    indice_q = Query[0].index(col1)
    indice_t = Tabela[0].index(col2)

    cont = 1

    # Para cada linha de uma tabela, a outra tabela gerará todas as suas linhas
    for q in Query[1:]:
        elem_q = q[indice_q]
        for t in Tabela[1:]:
            if (elem_q == t[indice_t]):
                QueryJoin.append(q.copy())
                QueryJoin[cont] += t.copy()
                cont = cont + 1
    
    return QueryJoin

# ON
def joinOn(Query, ListaTabelasNome, ListaTabelas):

    string = ''
    for palavra in com_on:
        string += palavra

    lista = string.replace('.',' ').replace('=',' ').split(' ')

    Auxiliares.removeElementosVazios(lista)

    primeira_coluna = lista[1]
    segunda_coluna = lista[-1]

    primeira_tabela = lista[0]
    segunda_tabela = lista[-2]

    nome_tabela = com_join[0]
    i = ListaTabelasNome.index(nome_tabela)
    # Simplesmente é copiada a tabela conforme o índice presente na lista de tabelas
    Tabela = ListaTabelas[i]

    if (nome_tabela == primeira_tabela):
        Auxiliares.trocaElementos(primeira_tabela, segunda_tabela)
        Auxiliares.trocaElementos(primeira_coluna, segunda_coluna)

    return join(Query, Tabela, primeira_coluna, segunda_coluna)

# USING
def joinUsing(Query, ListaTabelasNome, ListaTabelas):

    string = ''
    for palavra in com_using:
        string += palavra

    lista = string.replace('(','').replace(')','').split(' ')

    Auxiliares.removeElementosVazios(lista)

    coluna = lista[0]

    nome_tabela = com_join[0]
    i = ListaTabelasNome.index(nome_tabela)

    # Simplesmente é copiada a tabela conforme o índice presente na lista de tabelas
    Tabela = ListaTabelas[i]

    QueryJoin = join(Query, Tabela, coluna, coluna)
    
    indice = QueryJoin[0].index(coluna)
    for q in QueryJoin:
        q.pop(indice)

    return QueryJoin

def joinWhere(Query):
    string = ''
    for palavra in com_where:
        string += palavra

    lista = string.replace('.',' ').replace('=',' ').split(' ')

    Auxiliares.removeElementosVazios(lista)

    primeira_coluna = lista[1]
    segunda_coluna = lista[-1]

    primeira_tabela = lista[0]
    segunda_tabela = lista[-2]

    if (com_from[1] == primeira_tabela):
        Auxiliares.trocaElementos(primeira_tabela, segunda_tabela)
        Auxiliares.trocaElementos(primeira_coluna, segunda_coluna)
    
    QueryJoin = [[]]

    QueryJoin.append(Query[0].copy())

    indice_1 = Query[0].index(primeira_coluna)
    Query[0][indice_1] = ' '
    indice_2 = Query[0].index(segunda_coluna)

    for q in Query[1:]:
        if (q[indice_1] == q[indice_2]):
            QueryJoin.append(q)


    return QueryJoin