import csv
from datetime import datetime

def quan_ly_thong_tin_hoc_sinh():
    danh_sach_hoc_sinh = []

    def xem_hoc_sinh():
        print("\n--- Danh sách học sinh ---")
        if not danh_sach_hoc_sinh:
            print("Danh sách học sinh trống.")
        else:
            for hs in danh_sach_hoc_sinh:
                print(f"Mã HS: {hs['ma_hoc_sinh']}, Họ đệm: {hs['ho_dem']}, "
                      f"Tên: {hs['ten']}, Tuổi: {hs['tuoi']}, "
                      f"Ngày sinh: {hs['ngay_sinh']}, SĐT: {hs['so_dien_thoai']}, "
                      f"Mã lớp: {hs['ma_lop']}")

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

            hoc_sinh = {
                "ma_hoc_sinh": ma_hoc_sinh,
                "ho_dem": ho_dem,
                "ten": ten,
                "tuoi": tuoi,
                "ngay_sinh": ngay_sinh.strftime('%d/%m/%Y'),
                "so_dien_thoai": so_dien_thoai,
                "ma_lop": ma_lop
            }
            danh_sach_hoc_sinh.append(hoc_sinh)
            print("Học sinh đã được thêm thành công.")
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")

    def xoa_hoc_sinh():
        print("\n--- Xóa học sinh ---")
        ma_hoc_sinh = input("Nhập mã học sinh cần xóa: ").strip()
        for hs in danh_sach_hoc_sinh:
            if hs["ma_hoc_sinh"] == ma_hoc_sinh:
                danh_sach_hoc_sinh.remove(hs)
                print("Học sinh đã được xóa thành công.")
                return
        print("Không tìm thấy học sinh với mã đã nhập.")

    def chinh_sua_hoc_sinh():
        ma_hoc_sinh = input("Nhập mã số học sinh cần chỉnh sửa: ").strip()
        for hs in danh_sach_hoc_sinh:
            if hs['ma_hoc_sinh'] == ma_hoc_sinh:
                hs['ho_dem'] = input("Nhập họ đệm mới: ").strip()
                hs['ten'] = input("Nhập tên mới: ").strip()
                try:
                    hs['tuoi'] = int(input("Nhập tuổi mới: "))
                except ValueError:
                    print("Tuổi phải là một số hợp lệ!")
                    return
                ngay_sinh_str = input("Nhập ngày sinh mới (dd/mm/yyyy): ").strip()
                try:
                    ngay_sinh = datetime.strptime(ngay_sinh_str, '%d/%m/%Y')
                    hs['ngay_sinh'] = ngay_sinh.strftime('%d/%m/%Y')
                except ValueError:
                    print("Ngày sinh không hợp lệ!")
                    return
                hs['so_dien_thoai'] = input("Nhập số điện thoại mới: ").strip()
                hs['ma_lop'] = input("Nhập mã lớp mới: ").strip()
                print("Thông tin học sinh đã được cập nhật.")
                return
        print("Không tìm thấy học sinh với mã số này!")

    def tim_kiem_hoc_sinh():
        ten_tim_kiem = input("Nhập tên học sinh cần tìm: ").strip()
        ket_qua = [hs for hs in danh_sach_hoc_sinh if ten_tim_kiem.lower() in hs['ten'].lower()]
        if ket_qua:
            print("Kết quả tìm kiếm:")
            for hs in ket_qua:
                print(f"{hs['ma_hoc_sinh']} - {hs['ho_dem']} {hs['ten']} - {hs['tuoi']} tuổi")
        else:
            print("Không tìm thấy học sinh nào!")

    def doc_danh_sach_tu_file():
        try:
            with open("Bai_tap_lon_nhom1/file_csv/ds_hoc_sinh.csv", mode="r", newline="") as open_file:
                csv_reader = csv.DictReader(open_file)
                danh_sach_hoc_sinh.clear()
                for row in csv_reader:
                    danh_sach_hoc_sinh.append({
                        "ma_hoc_sinh": row['ma_hoc_sinh'],
                        "ho_dem": row['ho_dem'],
                        "ten": row['ten'],
                        "tuoi": int(row['tuoi']),
                        "ngay_sinh": row['ngay_sinh'],
                        "so_dien_thoai": row['so_dien_thoai'],
                        "ma_lop": row['ma_lop']
                    })
            print("Đọc danh sách học sinh từ file thành công.")
        except FileNotFoundError:
            print("File không tồn tại.")
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")

    def luu_danh_sach_vao_file():
        try:
            with open("Bai_tap_lon_nhom1/file_csv/ds_hoc_sinh.csv", mode="w", newline="") as open_file:
                fieldnames = ["ma_hoc_sinh", "ho_dem", "ten", "tuoi", "ngay_sinh", "so_dien_thoai", "ma_lop"]
                csv_writer = csv.DictWriter(open_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                for hs in danh_sach_hoc_sinh:
                    csv_writer.writerow(hs)
            print("Lưu danh sách học sinh vào file thành công.")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi lưu file: {e}")

    while True:
        print("\n--- Quản lý thông tin học sinh ---")
        print("1. Xem danh sách học sinh")
        print("2. Thêm học sinh")
        print("3. Xóa học sinh")
        print("4. Chỉnh sửa thông tin học sinh")
        print("5. Tìm kiếm học sinh")
        print("6. Lưu danh sách vào file")
        print("7. Đọc danh sách từ file")
        print("8. Thoát")

        try:
            lua_chon = int(input("Chọn chức năng (1-8): "))
            if lua_chon == 1:
                xem_hoc_sinh()
            elif lua_chon == 2:
                them_hoc_sinh()
            elif lua_chon == 3:
                xoa_hoc_sinh()
            elif lua_chon == 4:
                chinh_sua_hoc_sinh()
            elif lua_chon == 5:
                tim_kiem_hoc_sinh()
            elif lua_chon == 6:
                luu_danh_sach_vao_file()
            elif lua_chon == 7:
                doc_danh_sach_tu_file()
            elif lua_chon == 8:
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        except ValueError:
            print("Vui lòng nhập số từ 1 đến 8.")
