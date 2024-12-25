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
