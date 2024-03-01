"""def busca_binaria(array,x,low,high):
    while low<=high:
        mid = low +(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low = mid +1
        else:
            high = mid - 1
    return -1


array=[3,4,5,6,7,8,9]
x=3
resultado= busca_binaria(array,x,0,len(array)-1)

if resultado != -1 :
    print("elemento está presente no index"+ str(resultado))
else:
    print("elemento não encontrado")"""




grafico = {
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

def dfs(visitado,grafico,no):
    if no not in visitado:
        print(no) # imprime o no atual
        visitado.add(no) # marca o nó atual como visitado
        for vizinho in grafico[no]:
            dfs(visitado,grafico,vizinho)
