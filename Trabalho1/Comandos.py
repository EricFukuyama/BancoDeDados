comando = "SELECT emp_no,first_name FROM employees Where emp_no = 10000 ORDER BY emp_no ;".replace(',', ' ').replace(';', '').replace('\'', ' ').replace('\"', ' ').rstrip(',').casefold().split()
#input("Qual o comando SQL?").replace(',', ' ').replace(';', '').replace('\'', ' ').replace('\"', ' ').rstrip(',').casefold().split()

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

#Chama as funcoes para fazer o select, from, where e orderby
def executarComando(ListaTabelasNome, ListaTabelas):
    # Gera tabela com todos os dados contidos em FROM
    Query = fromTudo(ListaTabelasNome, ListaTabelas)
    
    #Gera tabela com os elementos que satisfazem o where
    Query = where(Query)
    
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

    mergeSort(Query, i)

    # Caso tenha colocado em ordem decrescente, é invertido a ordem dos elementos
    try:
        if (com_order[1] == "desc"):
            Query.reverse()
    except:
        i = -1

    # Após ordenado, é inserida novamente
    Query.insert(0, atributos)

    return Query

# MergeSort in Python (adaptação do código presente em https://www.programiz.com/dsa/merge-sort)
def mergeSort(array, index):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L, index)
        mergeSort(M, index)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            # Único trecho de código que precisou ser adaptado
            if L[i][index] < M[j][index]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

#procura qual é a operação entre >,<,<=,>=,!=,=
def procuraWhere(comando):
    if(comando.find(">")>1):
        if(comando[comando.find(">")+1]=="="):
            comando=comando.split(">=")
            comando.append(">=")
        else:
            comando=comando.split(">")
            comando.append(">")
    elif(comando.find("<")>1):
        if(comando[comando.find("<")+1]=="="):
            comando=comando.split("<=")
            comando.append("<=")
        elif(comando[comando.find("<")+1]==">"):
            comando=comando.split("<>")
            comando.append("!=")
        else:
            comando=comando.split("<")
            comando.append("<")
    elif(comando.find("=")>1):
        if(comando[comando.find("=")-1]=='!'):
            comando=comando.split("!=")
            comando.append("!=")
        else:
            comando=comando.split("=")
            comando.append("=")
    for i in range(len(comando)):
        comando[i]=comando[i].strip()
        try: 
            comando[i]=int(comando[i])
        except:
            comando[i]=comando[i]
    #comando é uma lista com tres posicoes, a primeira tem o primeiro elemento que será comparado, 
    # a segunda posicao o segundo elemento e a terceira qual é a operacao comparativa 
    return(comando)

#faz a comparacao entre os elementos e verifica se eh verdadeira
def comparacao(Condicao, Indice, Indice2, Query, i):
    #se for string o elemento da tabela
    try:
        if(Indice>-1 and Indice2>-1):
            if(Condicao[2]=='>'):
                if Query[i][Indice].casefold()>Query[i][Indice2].casefold():
                    return True
            elif(Condicao[2]=='>='):
                if Query[i][Indice].casefold()>=Query[i][Indice2].casefold():
                    return True
            elif(Condicao[2]=='<'):
                if Query[i][Indice].casefold()<Query[i][Indice2].casefold():
                    return True
            elif(Condicao[2]=='<='):
                if Query[i][Indice].casefold()<=Query[i][Indice2].casefold():
                    return True
            elif(Condicao[2]=='='):
                if Query[i][Indice].casefold()==Query[i][Indice2].casefold():
                    return True
            elif(Condicao[2]=='!='):
                if Query[i][Indice].casefold()<Query[i][Indice2].casefold():
                    return True
                        
        elif(Indice>-1):
            if(Condicao[2]=='>'):
                if Query[i][Indice].casefold()>Condicao[1]:
                    return True
            elif(Condicao[2]=='>='):
                if Query[i][Indice].casefold()>=Condicao[1]:
                    return True
            elif(Condicao[2]=='<'):
                if Query[i][Indice].casefold()<Condicao[1]:
                    return True
            elif(Condicao[2]=='<='):
                if Query[i][Indice].casefold()<=Condicao[1]:
                    return True
            elif(Condicao[2]=='='):
                if Query[i][Indice].casefold()==Condicao[1]:
                    return True
            elif(Condicao[2]=='!='):
                if Query[i][Indice].casefold()<Condicao[1]:
                    return True
            
        elif(Indice2>-1):
            if(Condicao[2]=='>'):
                if Condicao[0]>Query[i][Indice2].casefold():
                    return True
            elif(Condicao[2]=='>='):
                if Condicao[0]>=Query[i][Indice2].casefold():
                    return True
            elif(Condicao[2]=='<'):
                if Condicao[0]<Query[i][Indice2].casefold():
                    return True
            elif(Condicao[2]=='<='):
                if Condicao[0]<=Query[i][Indice2].casefold():
                    return True
            elif(Condicao[2]=='='):
                if Condicao[0]==Query[i][Indice2].casefold():
                    return True
            elif(Condicao[2]=='!='):
                if Condicao[0]<Query[i][Indice2].casefold():
                    return True
        
        else:
            if(Condicao[2]=='>'):
                if Condicao[0]>Condicao[1]:
                    return True
            elif(Condicao[2]=='>='):
                if Condicao[0]>=Condicao[1]:
                    return True
            elif(Condicao[2]=='<'):
                if Condicao[0]<Condicao[1]:
                    return True
            elif(Condicao[2]=='<='):
                if Condicao[0]<=Condicao[1]:
                    return True
            elif(Condicao[2]=='='):
                if Condicao[0]==Condicao[1]:
                    return True
            elif(Condicao[2]=='!='):
                if Condicao[0]<Condicao[1]:
                    return True
    #realiza as comparacoes se for int
    except:
        if(Indice>-1 and Indice2>-1):
            if(Condicao[2]=='>'):
                if Query[i][Indice]>Query[i][Indice2]:
                    return True
            elif(Condicao[2]=='>='):
                if Query[i][Indice]>=Query[i][Indice2]:
                    return True
            elif(Condicao[2]=='<'):
                if Query[i][Indice]<Query[i][Indice2]:
                    return True
            elif(Condicao[2]=='<='):
                if Query[i][Indice]<=Query[i][Indice2]:
                    return True
            elif(Condicao[2]=='='):
                if Query[i][Indice]==Query[i][Indice2]:
                    return True
            elif(Condicao[2]=='!='):
                if Query[i][Indice]<Query[i][Indice2]:
                    return True
                        
        elif(Indice>-1):
            if(Condicao[2]=='>'):
                if Query[i][Indice]>Condicao[1]:
                    return True
            elif(Condicao[2]=='>='):
                if Query[i][Indice]>=Condicao[1]:
                    return True
            elif(Condicao[2]=='<'):
                if Query[i][Indice]<Condicao[1]:
                    return True
            elif(Condicao[2]=='<='):
                if Query[i][Indice]<=Condicao[1]:
                    return True
            elif(Condicao[2]=='='):
                if Query[i][Indice]==Condicao[1]:
                    return True
            elif(Condicao[2]=='!='):
                if Query[i][Indice]<Condicao[1]:
                    return True
            
        elif(Indice2>-1):
            if(Condicao[2]=='>'):
                if Condicao[0]>Query[i][Indice2]:
                    return True
            elif(Condicao[2]=='>='):
                if Condicao[0]>=Query[i][Indice2]:
                    return True
            elif(Condicao[2]=='<'):
                if Condicao[0]<Query[i][Indice2]:
                    return True
            elif(Condicao[2]=='<='):
                if Condicao[0]<=Query[i][Indice2]:
                    return True
            elif(Condicao[2]=='='):
                if Condicao[0]==Query[i][Indice2]:
                    return True
            elif(Condicao[2]=='!='):
                if Condicao[0]<Query[i][Indice2]:
                    return True
        
        else:
            if(Condicao[2]=='>'):
                if Condicao[0]>Condicao[1]:
                    return True
            elif(Condicao[2]=='>='):
                if Condicao[0]>=Condicao[1]:
                    return True
            elif(Condicao[2]=='<'):
                if Condicao[0]<Condicao[1]:
                    return True
            elif(Condicao[2]=='<='):
                if Condicao[0]<=Condicao[1]:
                    return True
            elif(Condicao[2]=='='):
                if Condicao[0]==Condicao[1]:
                    return True
            elif(Condicao[2]=='!='):
                if Condicao[0]<Condicao[1]:
                    return True

def where(Query):
    
    #verifica se a lista está vazia
    if(len(com_where)==0):
        return Query
    
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
        condicao.append(procuraWhere(comando[0]))
        condicao.append(procuraWhere(comando[1]))
        condicao.append("and")

    #verifica se há comando OR
    elif(comando.find(" or ")>0):
        comando = comando.split("or")
        condicao.append(procuraWhere(comando[0]))
        condicao.append(procuraWhere(comando[1]))
        condicao.append("or")

    #Caso não tenha and e or
    else:
        condicao.append(procuraWhere(comando))    
        
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
            if(comparacao(condicao[0], indice, indice2, Query, i)):
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
                if(comparacao(condicao[0], indice, indice2, Query, i) and comparacao(condicao[1], indice3, indice4, Query, i)):
                    novaQuery.append(Query[i])
        
        if condicao[2]=='or':
            for i in range(1,len(Query)):
                if(comparacao(condicao[0], indice, indice2, Query, i) or comparacao(condicao[1], indice3, indice4, Query, i)):
                    novaQuery.append(Query[i])
        
    return(novaQuery)
