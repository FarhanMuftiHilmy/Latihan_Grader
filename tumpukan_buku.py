#==============================================================================
# n = int(input())
# buku = []
# 
# def isEmpty():
#     return  inputs == []
# 
# for i in range(n):
#     inputs = list(input().split())
#     
#     if inputs[0] == "A" and not isEmpty():
#         buku.pop()
#     elif inputs[0] == "T":
#         buku.append(inputs)
# 
# for i in range(len(buku)):
#     buku[i].pop(0)
# 
# for i in range(len(buku)):    
#     print(" ".join(buku.pop()))
#==============================================================================

def isEmpty():
    return kode == []

n = int(input())

kode = []
judul = []

for i in range(n):
    masukan = list(input().split())
    
    if (masukan[0] == "T"):
        kode.append(masukan[1])
        judul.append(masukan[2])
    elif (not isEmpty() and masukan[0] == "A"):
        kode.pop()
        judul.pop()

for i in range(len(kode)):
    print(kode.pop(), judul.pop())
            