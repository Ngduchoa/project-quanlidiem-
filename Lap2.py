

chuoi = f'''
    Kiếp con người mỏng manh như là gió
    Sống trên đời có được mấy lần vui
    Sao phải đau mà không thể mỉm cười
    Gắng buông nỗi ngậm ngùi nơi quá khứ

    Nếu có thể sao ta không làm thử
    Để tâm hồn khắc hai chữ bình an
    Cho đôi chân bước thanh thản nhẹ nhàng
    Dù hướng đời có muôn ngàn đá sỏi
'''
work = "con người"

# if work in chuoi :
#     print(f"Tu {work} o trong chuoi")
#     start_index = chuoi.find(work)
#     end_index = chuoi.find(work) + len(work)
#     extract_upper = chuoi[start_index:end_index].upper()
#     print(extract_upper)
# else :
#     print(f"Tu {work} khong co trong chuoi")


work1 = "bình an"
work2 = "hạnh phúc"
extract_replace = chuoi.replace(work1,work2)
a = '''...\n'''
chuoi_moi= f"{a}{chuoi}\n{a}"
print(chuoi_moi)





