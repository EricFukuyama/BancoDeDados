#Daniel Augusto Pires de Castro
#Eric Yutaka Fukuyama

import Comandos

def criarTabela(csvTabela):
    # Abre arquivo dado o caminho de entrada e assim é criada uma tabela conforme sintaxe de arquivo csv
    with open(csvTabela, 'r') as f:
        results = []
        for line in f:
            line = line.rstrip('\n')
            atributos = line.split(',')
            for i in range(len(atributos)):
                atributos[i] = atributos[i].strip('"')
            results.append((atributos[:]))
    return results, len(atributos)
                
#Caminho = "/home/eric/Documentos/UTFPR/BancoDeDados/Trabalho1"
Caminho = "C:\\Users\\danie\\Documents\\Faculdade\\2022.2\\Introducao a Banco de Dados\\Trabalho1"

#input("Qual a pasta que está as tabelas?")
ListaTabelasNome = ["departments", "employees_copy"]
#input("Nome de quais tabelas serão usadas?").split()
QtdeAtributos=[]
ListaTabelas=[]

# Chama função de criar tabela para cada uma digitada e assim são colocadas em lista
for tabela in ListaTabelasNome:
    (a, b) = criarTabela(Caminho+'/'+tabela+'.csv')
    QtdeAtributos.append(b)
    ListaTabelas.append(a)
    
#comando = input("Qual o comando SQL?")

# Funções chamadas
Comandos.printarComando()
Comandos.executarComando(ListaTabelasNome, ListaTabelas, QtdeAtributos)




""" CÓDIGOS RECICLÁVEIS ABAIXO """

# for i in range(len(ListaTabelas)):
#     print((ListaTabelas[i])[:][1])
#     print(len(ListaTabelas[i]))

# with open('employees1000.csv', 'r') as f:
#     results = []
#     quantidade = 0
#     flag = 0
#     for line in f:
#         line = line.rstrip('\n')
#         words = line.split(',')
#         for i in range(6):
#             words[i] = words[i].strip('"')
#         results.append((words[:]))
#         quantidade +=1
    
#     tipo = input("Procura por id(i) ou sobrenome(s)? ")
    
#     if(tipo == 'i'):
#         procurando = input("id: ")
#         for i in range(1,quantidade):
#             if results[i][0]==procurando:
#                 flag+=1
#                 print(results[0][0]+": "+results[i][0]+" "+results[0][1]+": "+results[i][1]+" "+results[0][2]+": "+results[i][2]+" "+results[0][3]+": "+results[i][3]+" "+results[0][4]+": "+results[i][4]+" "+results[0][5]+": "+results[i][5])
#     elif(tipo=='s'):
#         procurando = input("Sobrenome: ")
#         for i in range(1,quantidade):
#             if str(results[i][3])==procurando:
#                 flag+=1
#                 print(results[0][0]+": "+results[i][0]+" "+results[0][1]+": "+results[i][1]+" "+results[0][2]+": "+results[i][2]+" "+results[0][3]+": "+results[i][3]+" "+results[0][4]+": "+results[i][4]+" "+results[0][5]+": "+results[i][5])

#     if flag==0:
#         print("Funcionario nao encontrado")