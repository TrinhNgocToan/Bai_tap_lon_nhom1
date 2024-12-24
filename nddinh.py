def xem_lop_hoc(ma_lop, ten_lop, tong_so_ban):
    print("Thông tin lớp học:")
    print(f"- Mã lớp: {ma_lop}")
    print(f"- Tên lớp: {ten_lop}")
    print(f"- Tổng số bàn: {tong_so_ban}")
    return ma_lop, ten_lop, tong_so_ban

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

def xoa_lop_hoc(danh_sach_lop_hoc):
    ma_lop = input("Nhập mã lớp cần xóa: ")
    if ma_lop in danh_sach_lop_hoc:
        danh_sach_lop_hoc_moi = {}
        for key in danh_sach_lop_hoc:
            if key != ma_lop:
                danh_sach_lop_hoc_moi[key] = danh_sach_lop_hoc[key]
        danh_sach_lop_hoc = danh_sach_lop_hoc_moi
        print(f"Lớp học với mã {ma_lop} đã được xóa!")
    else:
        print(f"Lớp học với mã {ma_lop} không tồn tại!")
    return danh_sach_lop_hoc
