arr=[1,7,5,4,8,6,2]
arr.sort()
uzunluk = len(arr)
if uzunluk % 2 == 1:
    ortanca = int((uzunluk - 1) / 2)
    print(arr[ortanca])
else:
    ortanca = int(((uzunluk / 2) + (uzunluk / 2 - 1)) / 2)
    print(arr[ortanca])
