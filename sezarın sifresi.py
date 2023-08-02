def caesarCipher(s, k):
    # Write your code here
    k = k % 26
    orjk = "abcdefghijklmnopqrstuvwxyz"
    orjb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sifreli = ""
    for i in s:
        if i in orjk:
            if (orjk.index(i) + k < 26):
                sifreli = sifreli + orjk[orjk.index(i) + k]
            else:
                sifreli = sifreli + orjk[orjk.index(i) - (26 - k)]
        elif i in orjb:
            if (orjb.index(i) + k < 26):
                sifreli = sifreli + orjb[orjb.index(i) + k]
            else:
                sifreli = sifreli + orjb[orjb.index(i) - (26 - k)]
        else:
            sifreli = sifreli + i
    return sifreli
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
