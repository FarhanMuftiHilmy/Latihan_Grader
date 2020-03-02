n = int(input())
ls_total = []
total = 0

def isEmpty(Q):
    if len(Q) == 0:
        return True
    else:
        return False
if n == 0:
    print(0)
else:
    for i in range(n):
        x = input()
        sep_x = x.split(" ")
        kode = sep_x[0]
        uang = int(sep_x[1])
        if kode == "0":        
            ls_total.append(uang)
        elif kode == "1":
            ls_total.insert(0, uang)
        elif kode == "2" and not isEmpty(ls_total):
            ls_total.pop()
        elif kode == "3" and not isEmpty(ls_total):
            ls_total.pop(0)
            
    for i in range(len(ls_total)):
        total += ls_total[i]
    print(total)