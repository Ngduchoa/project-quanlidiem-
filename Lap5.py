
gia_ban_nuoc = (7500, 8800, 12000, 24000)

def tienbannuoc():
   san_luong = float(input("NHap so luong nuoc su dung:"))

   if san_luong <= 10 :
      tien_nuoc = san_luong * gia_ban_nuoc[0]
   elif san_luong <=20 :
      tien_nuoc = 10 * gia_ban_nuoc[0] + (san_luong - 10)*gia_ban_nuoc[1]
   elif san_luong <= 30 : 
      tien_nuoc = 10 * gia_ban_nuoc[0] + 10*gia_ban_nuoc[1] + (san_luong - 20)*gia_ban_nuoc[2]
   else :
      tien_nuoc = 10 * gia_ban_nuoc[0] + 10*gia_ban_nuoc[1] + 10*gia_ban_nuoc[2] + (san_luong -30)*gia_ban_nuoc[3]

   print(f"Tien nuoc cho {san_luong} m3 la {tien_nuoc}")


tienbannuoc()

# 
# NL_banh_dau = {"Duong" : 0.04 ,"Dau" : 0.07 }
# NL_banh_thapcam = {"Duong" : 0.06 ,"Dau" : 0.00}
# NL_banh_deo = {"Duong" : 0.05 ,"Dau" : 0.02}

# def nguyen_lieu_lam_banh(banh_dau,banh_thap,banh_deo):
#    Duong = banh_dau*0.04 + banh_thap*0.06 + banh_deo*0.05
#    Dau = banh_dau*0.07 + banh_thap*0 + banh_deo*0.02

#    nguyen_lieu = {"Sugar": Duong ,"Bean" : Dau}
#    return nguyen_lieu

# ketqua = nguyen_lieu_lam_banh(2,3,4)
# print(ketqua)
