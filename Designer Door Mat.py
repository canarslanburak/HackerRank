def sekil(N,M):
    cizgi = "-"
    desen = ".|."
    desensayisi = 1
    w = "WELCOME"

    for i in range(1, int((N + 1) / 2)):
        x = desen * desensayisi
        desensayisi += 2
        y = int((M - len(x)) / 2)
        print(cizgi * y + x + cizgi * y)

    print(cizgi * (int((M - len(w)) / 2)) + w + cizgi * (int((M - len(w)) / 2)))

    for i in range(int((N + 1) / 2), 1, -1):
        x = desen * (desensayisi - 2)
        desensayisi -= 2
        y = int((M - len(x)) / 2)
        print(cizgi * y + x + cizgi * y)
if __name__ == '__main__':
    N,M,*line = input().split()
    N=int(N)
    M=int(M)
    sekil=sekil(N,M)