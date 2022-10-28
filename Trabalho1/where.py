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
        if(comando[comando.find("<")-1]):
            comando=comando.split("!=")
            comando.append("!=")
        else:
            comando=comando.split("=")
            comando.append("=")
    for i in range(len(comando)):
        comando[i]=comando[i].strip()
    return(comando)

comando = "from_date>2000 AND  to_date < 1000".casefold().split()
comando = " ".join(comando)
condicao=[]

if(comando.find(" and ")>0):
    comando = comando.split(" and ")
    condicao.append(procuraWhere(comando[0]))
    condicao.append(procuraWhere(comando[1]))
    condicao.append("and")

elif(comando.find(" or ")>0):
    comando = comando.split("or")
    condicao.append(procuraWhere(comando[0]))
    condicao.append(procuraWhere(comando[1]))
    condicao.append("or")

else:
    condicao.append(procuraWhere(comando))
    

print(condicao)

