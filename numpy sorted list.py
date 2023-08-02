import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    liste1=[]
    liste2=[]
    for i in arr:
        if float(i) <=0:
            liste1.append(float(i))
        else:
            liste2.append(float(i))
    liste1.sort()
    liste2.sort()
    liste2=liste2[::-1]
    liste3=liste1+liste2
    a=numpy.array(liste3,float)
    return a
arr = input().strip().split(' ')
result = arrays(arr)
print(result)