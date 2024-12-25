lop_hoc = [
    {"ma_sinh_vien": "SV001", "name": "Nguyen Van A", "so_diem": 90},
    {"ma_sinh_vien": "SV002", "name": "Tran Thi B", "so_diem": 75},
    {"ma_sinh_vien": "SV003", "name": "Le Van C", "so_diem": 88}
]
def tim_diem_dua_tren_ma_hoc_sinh(lop_hoc, ma_sinh_vien ):
    for student in lop_hoc:
        if student["ma_sinh_vien"] == ma_sinh_vien:
            return student["so_diem"]  # Trả về điểm của sinh viên
    return None  # Nếu không tìm thấy sinh viên với mã này

ma_sinh_vien = "SV003"
so_diem = tim_diem_dua_tren_ma_hoc_sinh(lop_hoc, ma_sinh_vien)

if so_diem is not None:
    print(f"Điểm của sinh viên có mã {ma_sinh_vien} là: {so_diem}")
else:
    print(f"Không tìm thấy sinh viên với mã {ma_sinh_vien}.")