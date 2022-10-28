#Daniel Augusto Pires de Castro
#Eric Yutaka Fukuyama

#Caminho = "/home/eric/Documentos/UTFPR/BancoDeDados/Trabalho1"
#Caminho = "C:\\Users\\danie\\Documents\\Faculdade\\2022.2\\Introducao a Banco de Dados\\BancoDeDados\\Trabalho1"
Caminho = input("Qual a pasta que está as tabelas? ")

#ListaTabelasNome = ["employees"]
ListaTabelasNome = input("Nome de quais tabelas serão usadas? Escrever entre espaços: ").split()

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
                try:
                    atributos[i]=int(atributos[i])
                except:
                    atributos[i]=atributos[i]
            results.append((atributos[:]))
    return results, len(atributos)

ListaTabelas=[]

# Chama função de criar tabela para cada uma digitada e assim são colocadas em lista
for tabela in ListaTabelasNome:
    (a, b) = criarTabela(Caminho+'/'+tabela+'.csv')
    ListaTabelas.append(a)

# Funções chamadas
#Comandos.printarComando()
Comandos.executarComando(ListaTabelasNome, ListaTabelas)