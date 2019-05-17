largura=int(input("Digite uma largura:"))
altura=int(input("Digite uma altura:"))

linha=1
coluna=1

while linha<=altura:
    while coluna<=largura:
        print("#",end="")
        coluna=coluna+1
    linha=linha+1
    print()
    coluna=1



