


sinh_vien_list = []  

while True :
     ten = input("Xin moi nhap ten : ")
     diem = float(input("Xin moi nhap diem :"))

     if diem >= 8.5 :
          xep_loai = " Xuat sac"
     elif diem >= 8 :
          xep_loai = "Gioi"
     elif diem >= 6.5 :
          xep_loai = "Kha"
     elif diem >= 5 :
          xep_loai = "Tb"
     else :
          xep_loai = "Yeu"

     # Luu thong tin sinh vien
     sinh_vien = {
          'Ten' : ten,
          'Diem' : diem,
          'XepLoai' : xep_loai
     }

     sinh_vien_list.append(sinh_vien)

     for sinh_vien in sinh_vien_list :
          print("Ten : ", sinh_vien["Ten"])
          print("Diem : ", sinh_vien["Diem"])
          print("Xep_loai : ", sinh_vien["XepLoai"])
          print()