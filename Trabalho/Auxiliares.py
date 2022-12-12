#Daniel Augusto Pires de Castro
#Eric Yutaka Fukuyama

# Esse arquivo contém funções auxiliares que não correspondem diretamente ao processo de cláusulas

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

# Função que permite limpar uma lista mantendo apenas o que é necessário
def removeElementosVazios(lista):
    i = len(lista)
    while(i > 0):
        try:
            lista.remove('')
        except:
            i = -1

# Clássica função para economizar 3 linhas
def trocaElementos(el1, el2):
    aux = el1
    el1 = el2
    el2 = aux

# Função que faz retornar a flag, realizando o ato de contar os elementos que devem ter em um where do tipo join
def detectaJoin(lista):
    i = 0
    string = ''
    for palavra in lista:
        string += palavra

    try:
        i += string.count('.')
        i += string.count('=')
    except:
        i = -1

    if i == 3:
        return True
    return False
