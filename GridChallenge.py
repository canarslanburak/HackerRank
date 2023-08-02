grid = ['mpxz', 'abcd', 'wlmf']
#grid = ["abc","hjk","mpq","rtv"]
grid2=[]
sayac = 0
for i in grid:
    grid2.append("".join(sorted(i)))
print(grid2)
for k in range(len(grid2)):
    for i in range(len(grid2[k])):
        kelime = ""
        for j in range(len(grid2)):
            kelime = kelime + grid2[j][i]
            print(kelime)
        if kelime == "".join(sorted(kelime)):
            sayac += 1
    if sayac == len(grid2[k]):
        print("YES")
        break
    else:
        print("NO")
        break