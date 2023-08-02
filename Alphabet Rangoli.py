def print_rangoli(size):
    # your code goes here
    #chr(97)=a anlamına geliyor
    uzunluk=4*n-3
    string=""
    for i in range(1,size+1):
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < uzunluk :
                string += '-'
        for k in range(i - 1, 0, -1):
            string += chr(97 + size - k)
            if len(string) < uzunluk:
                string += '-'
        print(string.center(uzunluk, '-'))
        string = ''

    for i in range(size - 1, 0, -1):
        string = ''
        for j in range(0, i):
            string += chr(96 + size - j)
            if len(string) < uzunluk:
                string += '-'
        for k in range(i - 1, 0, -1):
            string += chr(97 + size - k)
            if len(string) < uzunluk:
                string += '-'
        print(string.center(uzunluk, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)