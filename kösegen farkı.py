a=[[11,2,4],[4,5,6],[10,8,-12]]
kosegen1=[]
kosegen2=[]
for j in range(len(a)):
    for k in range(len(a)):
        if k==j:
            kosegen1.append(a[j][k])
        if k+j==(len(a)-1):
            kosegen2.append(a[j][k])
toplam1=sum(kosegen1)
toplam2=sum(kosegen2)
print(kosegen1,kosegen2)
print(abs(toplam1-toplam2))