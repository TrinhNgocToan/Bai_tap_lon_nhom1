# hàm chỉnh sửa thông tin
def chinh_sua_hoc_sinh():
    ma_so = input("Nhập mã số học sinh cần chỉnh sửa: ")
    for hs in danh_sach_hoc_sinh:
        if hs['id'] == ma_so:     #là mã số của hs muốn xóa đấy
            hs['ten'] = input("Nhập tên mới: ")
            hs['tuoi'] = input("Nhập tuổi mới: ")
            print("Thông tin học sinh đã được cập nhật.")
            return
    print("Không tìm thấy học sinh với mã số này!")


#hàm tìm kiếm 
def tim_kiem_hoc_sinh():
    ten_tim_kiem = input("Nhập tên học sinh cần tìm: ")
    ket_qua = [hs for hs in danh_sach_hoc_sinh if ten_tim_kiem.lower() in hs['ten'].lower()]
    if ket_qua:
        print("Kết quả tìm kiếm:")
        for hs in ket_qua:
            print(f"{hs['id']} - {hs['ten']} - {hs['tuoi']} tuổi")
    else:
        print("Không tìm thấy học sinh nào!")



# từ đây xuống dưới là đọc và lưu file
def doc_danh_sach_tu_file():
    try:
        with open("ds_hoc_sinh.csv", mode="r") as file: 
            reader = csv.DictReader(file)
            danh_sach_hoc_sinh = list(reader)
            print("Đã đọc danh sách học sinh từ file.")
            return danh_sach_hoc_sinh
    except FileNotFoundError:
        print("File ds_hoc_sinh.csv chưa tồn tại!")
        return []  # cái này là trả về danh sách rỗng nếu file không tồn tại





# 7. Hàm lưu danh sách vào file CSV
def luu_danh_sach_vao_file(danh_sach_hoc_sinh):
    with open("ds_hoc_sinh.csv", mode="w", newline="") as file: 
        fieldnames = ["id", "ten", "tuoi"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(danh_sach_hoc_sinh)
        print("Đã lưu danh sách học sinh vào file.")