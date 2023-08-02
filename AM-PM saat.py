s="12:45:54PM"
ek=s[8:].split(":")
zaman = s[:-2].split(":") #['07', '05', '45']
if ek[0]=="PM" and int(zaman[0])!=12:
    zaman[0] = int(zaman[0]) + 12
    zaman[0] = str(zaman[0])
    saat = ":".join(zaman)
    print(saat)
elif ek[0]=="PM" :
    zaman[0] = int(zaman[0])
    zaman[0] = str(zaman[0])
    saat = ":".join(zaman)
    print(saat)
elif (ek[0]=="AM" and int(zaman[0])<12):
    zaman[0] = int(zaman[0])
    zaman[0] = "0"+str(zaman[0])
    saat = ":".join(zaman)
    print(saat)
else:
    zaman[0] = int(zaman[0]) - 12
    zaman[0] = str(zaman[0])+"0"
    saat = ":".join(zaman)
    print(saat)