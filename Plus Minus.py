arr= [-4, 3, -9, 0, 4, 1]
n,p,s=0,0,0
for i in arr:
    if i <0:
        n+=1
    elif i>0:
        p+=1
    else:
        s+=1
print(p,n,s)
p_oran=p/len(arr)
p_oran=round(p_oran,6)
n_oran=n/len(arr)
n_oran=round(n_oran,6)
s_oran=s/len(arr)
s_oran=round(s_oran,6)
print("{:6f}".format(p_oran))
print("{:6f}".format(n_oran))
print("{:6f}".format(s_oran))