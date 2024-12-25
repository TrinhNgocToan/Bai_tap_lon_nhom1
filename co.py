

def xem_hoc_sinh():
    print("\n--- Danh sách học sinh ---")
    if not students:
        print("Danh sách học sinh trống.")
    else:
        for student in students:
            print(f"Mã HS: {student['ma_hoc_sinh']}, Họ đệm: {student['ho_dem']}, "
                  f"Tên: {student['ten']}, Tuổi: {student['tuoi']}, "
                  f"Ngày sinh: {student['ngay_sinh']}, SĐT: {student['so_dien_thoai']}, "
                  f"Mã lớp: {student['ma_lop']}")

def them_hoc_sinh():
    print("\n--- Thêm học sinh ---")
    try:
        ma_hoc_sinh = input("Nhập mã học sinh (tối đa 10 ký tự): ").strip()
        ho_dem = input("Nhập họ đệm (tối đa 50 ký tự): ").strip()
        ten = input("Nhập tên (tối đa 50 ký tự): ").strip()
        tuoi = int(input("Nhập tuổi: "))
        ngay_sinh_str = input("Nhập ngày tháng năm sinh (dd/mm/yyyy): ").strip()
        ngay_sinh = datetime.strptime(ngay_sinh_str, '%d/%m/%Y')
        so_dien_thoai = input("Nhập số điện thoại (10 ký tự): ").strip()
        ma_lop = input("Nhập mã lớp (tối đa 10 ký tự): ").strip()

        student = {
            "ma_hoc_sinh": ma_hoc_sinh,
            "ho_dem": ho_dem,
            "ten": ten,
            "tuoi": tuoi,
            "ngay_sinh": ngay_sinh.strftime('%d/%m/%Y'),
            "so_dien_thoai": so_dien_thoai,
            "ma_lop": ma_lop
        }
        students.append(student)
        print("Học sinh đã được thêm thành công.")
    except ValueError:
        print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")

def xoa_hoc_sinh():
    print("\n--- Xóa học sinh ---")
    ma_hoc_sinh = input("Nhập mã học sinh cần xóa: ").strip()
    for student in students:
        if student["ma_hoc_sinh"] == ma_hoc_sinh:
            students.remove(student)
            print("Học sinh đã được xóa thành công.")
            return
    print("Không tìm thấy học sinh với mã đã nhập.")
