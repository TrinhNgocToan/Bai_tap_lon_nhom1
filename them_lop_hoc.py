def them_lop_hoc(danh_sach_lop_hoc):
    ma_lop = str(input("Nhập mã lớp: "))
    ten_lop = str(input("Nhập tên lớp: "))
    so_ban = int(input("Nhập số bàn: "))
    danh_sach_lop_hoc[ma_lop] = {
        'Tên lớp': ten_lop,
        'Số bàn': so_ban
    }
    print(f"Lớp học {ten_lop} đã được thêm!")
    return danh_sach_lop_hoc
