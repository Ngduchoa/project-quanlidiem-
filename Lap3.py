# day_so = [9, 59, 21, 9, 20, 23, 19, 12, 19, 77]
# day_so.sort()
# tong = 0
# so_dem = 0
# for i in day_so:
#     if  i % 3 == 0 :
#         tong += i 
#         so_dem += 1

# if so_dem > 0:
#     trung_binh = tong/so_dem
#     print("Trung Binh so chia het cho 3 la : " , trung_binh)
# else :
#     print("Khong co so chia het cho 3")

# # Thay đổi sắp xếp theo thứ tự giảm dần, khi đó phần tử nhỏ nhất trong danh
# # sách sẽ là phần tử thứ mấy?

# day_so.sort(reverse=True)
# vi_tri_cua_phan_tu_min = len(day_so) - 1
# print(vi_tri_cua_phan_tu_min)



# HoTen = input("Xin Moi Nhap Ten :" )
# Diem = float(input("Xin Moi Nhap Diem :" ))

# ThongTin = {
#     'HoTen' : HoTen,
#     'Diem' : Diem
# }
# if ThongTin['Diem'] >= 9 :
#             ThongTin['XepLoai'] = "XuatSac"
# elif ThongTin['Diem'] >= 8 :
#             ThongTin['XepLoai'] = "Gioi"
# elif ThongTin['Diem'] >= 7 :
#             ThongTin['XepLoai'] = "Kha"
# elif ThongTin['Diem'] >=5 :
#             ThongTin['XepLoai'] = "TrungBinh"
# else :
#     ThongTin['XepLoai'] = "Yeu"


# print("HoTen : ", ThongTin['HoTen'])
# print("Diem : " , ThongTin['Diem'])
# print("XepLoai :" , ThongTin['XepLoai'])

# Bài 3 (2 điểm)
# Viết chương trình nhập một số nguyên từ bàn phím và cho biết số đó có phải là số
# nguyên tố hay không (số nguyên tố là số chỉ chia hết cho 1 và chính nó).

def songuyento(n):
    n <= 1
    return False

ok = True
i =2

while i < (n-1) :
    if n % i == 0:
        ok = False
        break
    i += 1

def main() :
     try:
        number = int(input("Nhap vao so nguyen to :"))
        if songuyento(number):
            print(f"So {number} la so nguyen to")
        else :
            print(f"So {number} khong phai so nguyen to")  
     except ValueError:
        print("Nhap vao khong phai so nguyen to")


if
     
     
    
        
   

      