jumlah = 0
prototype = []
ls_tabung = []
n = int(input())
def cetak(x):
    for i in range(len(x)):
        print(x[i], end=" ")
    print()
prototype = list(map(str,input().split()))

for i in range(len(prototype)):    
    jumlah += 1
    if jumlah == 1:
        ls_tabung.append(prototype[i])
    elif jumlah%2 != 0:
        ls_tabung.insert(int(len(ls_tabung)//2), prototype[i])
    elif jumlah%2 == 0:
        ls_tabung.insert(int(len(ls_tabung)//2), prototype[i])
    

cetak(ls_tabung)
    
        