if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    liste=[]
    liste2=[]
    for i in range(x+1):
        for k in range(y+1):
            for m in range(z+1):
                liste.append([i]+[k]+[m])
    for sayac in range(len(liste)):
        if (sum(liste[sayac])!=n):
            liste2.append(liste[sayac])
    print(liste2)