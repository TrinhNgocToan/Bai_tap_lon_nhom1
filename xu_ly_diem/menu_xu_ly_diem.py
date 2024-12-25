import csv
from datetime import datetime

def menu_xu_ly_diem_hoc_sinh():
    danh_sach_hoc_sinh = []  # Tạo danh sách học sinh để sử dụng trong các chức năng

    def nhap_danh_sach_hoc_sinh():
        danh_sach = []
        so_luong = int(input("Nhập số lượng học sinh: "))

        for i in range(so_luong):
            print(f"Nhập thông tin cho học sinh thứ {i + 1}:")
            ma_hoc_sinh = input("Mã học sinh: ")
            ho_va_ten = input("Họ và tên: ")
            tuoi = int(input("Tuổi: "))
            ngay_sinh = input("Ngày sinh (dd/mm/yyyy): ")
            ngay_sinh = datetime.strptime(ngay_sinh, '%d/%m/%Y')
            so_dien_thoai = input("Số điện thoại: ")
            lop = input("Lớp: ")
            diem_toan = float(input("Điểm Toán: "))
            diem_ly = float(input("Điểm Lý: "))
            diem_hoa = float(input("Điểm Hóa: "))
            diem_tb = (diem_toan + diem_ly + diem_hoa) / 3

            thong_tin_hoc_sinh = {
                "ma_hoc_sinh": ma_hoc_sinh,
                "ho_va_ten": ho_va_ten,
                "tuoi": tuoi,
                "ngay_sinh": ngay_sinh.strftime('%d/%m/%Y'),
                "so_dien_thoai": so_dien_thoai,
                "lop": lop,
                "diem_toan": diem_toan,
                "diem_ly": diem_ly,
                "diem_hoa": diem_hoa,
                "diem_tb": diem_tb
            }

            danh_sach.append(thong_tin_hoc_sinh)

        return danh_sach

    def hien_thi_danh_sach_hoc_sinh(danh_sach):
        if not danh_sach:
            print("Danh sách học sinh trống.")
            return

        print("Mã HS | Họ và tên       | Tuổi | Ngày sinh | SĐT       | Lớp | Toán | Lý | Hóa | Điểm TB")
        print("-" * 80)
        for hs in danh_sach:
            print(f"{hs['ma_hoc_sinh']} | {hs['ho_va_ten']:<15} | {hs['tuoi']}   | {hs['ngay_sinh']} | {hs['so_dien_thoai']:<10} | {hs['lop']} | {hs['diem_toan']:.1f} | {hs['diem_ly']:.1f} | {hs['diem_hoa']:.1f} | {hs['diem_tb']:.2f}")

    def luu_file_csv(danh_sach):
        if not danh_sach:
            print("Danh sách trống, không có gì để lưu.")
            return

        with open("file_csv/ds_diem.csv", mode="w", newline="") as open_file:
            csv_writer = csv.writer(open_file)
            csv_writer.writerow(danh_sach[0].keys())  # Ghi header
            for hs in danh_sach:
                csv_writer.writerow(hs.values())
        print("Lưu danh sách học sinh thành công.")

    def doc_file_csv():
        danh_sach = []
        try:
            with open("file_csv/ds_diem.csv", mode="r") as open_file:
                csv_reader = csv.DictReader(open_file)
                for row in csv_reader:
                    row["tuoi"] = int(row["tuoi"])
                    row["diem_toan"] = float(row["diem_toan"])
                    row["diem_ly"] = float(row["diem_ly"])
                    row["diem_hoa"] = float(row["diem_hoa"])
                    row["diem_tb"] = float(row["diem_tb"])
                    danh_sach.append(row)
        except FileNotFoundError:
            print("Chưa có tệp dữ liệu.")

        return danh_sach

    def sua_diem_hoc_sinh(danh_sach):
        ma_hoc_sinh = input("Nhập mã học sinh cần sửa điểm: ")
        for hs in danh_sach:
            if hs['ma_hoc_sinh'] == ma_hoc_sinh:
                print(f"Sửa điểm cho học sinh {hs['ho_va_ten']}:")
                hs['diem_toan'] = float(input("Nhập điểm Toán mới: "))
                hs['diem_ly'] = float(input("Nhập điểm Lý mới: "))
                hs['diem_hoa'] = float(input("Nhập điểm Hóa mới: "))
                hs['diem_tb'] = (hs['diem_toan'] + hs['diem_ly'] + hs['diem_hoa']) / 3
                print("Đã cập nhật điểm thành công.")
                return
        print("Không tìm thấy học sinh với mã này.")

    while True:
        print("\nMenu:")
        print("1. Hiển thị danh sách học sinh")
        print("2. Nhập danh sách học sinh")
        print("3. Lưu danh sách vào tệp CSV")
        print("4. Sửa điểm của học sinh")
        print("5. Đọc danh sách từ file CSV")
        print("0. Thoát")

        lua_chon = input("Nhập lựa chọn: ")

        if lua_chon == "1":
            hien_thi_danh_sach_hoc_sinh(danh_sach_hoc_sinh)
        elif lua_chon == "2":
            danh_sach_hoc_sinh += nhap_danh_sach_hoc_sinh()
        elif lua_chon == "3":
            luu_file_csv(danh_sach_hoc_sinh)
        elif lua_chon == "4":
            sua_diem_hoc_sinh(danh_sach_hoc_sinh)
        elif lua_chon == "5":
            danh_sach_hoc_sinh = doc_file_csv()
        elif lua_chon == "0":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy thử lại.")
