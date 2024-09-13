gia_ban_nuoc = (7500, 8800, 12000, 24000)


def tinh_gia_ban(n):
    if n <= 10 :
        tien_nuoc = n * gia_ban_nuoc[0]
    elif n <= 20:
        tien_nuoc = n * gia_ban_nuoc[0] +  (n - 10)*gia_ban_nuoc[1]
    elif n <=30 :
        tien_nuoc =  10 * gia_ban_nuoc[0] +  10 * gia_ban_nuoc[1] + (n - 20)*gia_ban_nuoc[2]
    else   :
        tien_nuoc = 10 * gia_ban_nuoc[0] +  10 * gia_ban_nuoc[1] + 10 *gia_ban_nuoc[2] + (n-30)*gia_ban_nuoc[3]

    return tien_nuoc

n = float(input("Moi nhap vao :"))

tien_nc = tinh_gia_ban(n)
print("Gia ban nuoc", tien_nc)