largura=int(input("Digite uma largura:"))
altura=int(input("Digite uma altura:"))

linha=1
coluna=1

while linha<=altura:
    print("#",end="")
    coluna=2
    while coluna<largura:
        if linha==1 or linha==altura:
            print("#", end="")
        else:
            print(end=" ")
        coluna=coluna+1
    print("#")
    linha=linha+1



