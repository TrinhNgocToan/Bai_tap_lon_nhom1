import csv
from datetime import datetime

def menu_xu_ly_diem_hoc_sinh():
    danh_sach_hoc_sinh = []  
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

    def tim_kiem_hoc_sinh_theo_lop_hoc_ky_nam(danh_sach):
        lop = input("Nhập lớp cần tìm kiếm: ")
        ket_qua = [hs for hs in danh_sach if hs['lop'] == lop]
        if not ket_qua:
            print("Không tìm thấy học sinh phù hợp.")
        else:
            hien_thi_danh_sach_hoc_sinh(ket_qua)

    def tim_kiem_theo_lop_hoac_ten_lop(danh_sach):
        tu_khoa = input("Nhập mã lớp hoặc tên lớp: ")
        ket_qua = [hs for hs in danh_sach if hs['lop'] == tu_khoa]
        if not ket_qua:
            print("Không tìm thấy học sinh phù hợp.")
        else:
            ket_qua.sort(key=lambda x: (x['ma_hoc_sinh'], x['diem_tb']))
            hien_thi_danh_sach_hoc_sinh(ket_qua)

    def xep_hoc_sinh_theo_toan_truong(danh_sach):
        tieu_chi = input("Sắp xếp theo (1. Điểm TB, 2. Mã HS): ")
        if tieu_chi == "1":
            danh_sach.sort(key=lambda x: x['diem_tb'], reverse=True)
        elif tieu_chi == "2":
            danh_sach.sort(key=lambda x: x['ma_hoc_sinh'])
        else:
            print("Lựa chọn không hợp lệ.")
            return

        hien_thi_danh_sach_hoc_sinh(danh_sach)

    def xep_loai_hoc_sinh(danh_sach):
        lop = input("Nhập lớp cần xếp loại: ")
        ket_qua = [hs for hs in danh_sach if hs['lop'] == lop]
        if not ket_qua:
            print("Không tìm thấy học sinh phù hợp.")
            return

        ket_qua.sort(key=lambda x: x['ma_hoc_sinh'])
        print("Xếp loại học sinh:")
        for hs in ket_qua:
            loai = "Giỏi" if hs['diem_tb'] >= 8 else "Khá" if hs['diem_tb'] >= 6 else "Trung bình"
            print(f"{hs['ma_hoc_sinh']} - {hs['ho_va_ten']} - {loai}")

    def top_hoc_sinh(danh_sach):
        so_hoc_sinh = len(danh_sach)
        if so_hoc_sinh < 10:
            print("Danh sách không đủ 10 học sinh để tìm top.")
            return

        danh_sach.sort(key=lambda x: x['diem_tb'], reverse=True)
        print("Top 10 học sinh có điểm trung bình cao nhất:")
        for hs in danh_sach[:10]:
            print(f"{hs['ma_hoc_sinh']} - {hs['ho_va_ten']} - {hs['diem_tb']:.2f}")

        print("\nTop 10 học sinh có điểm trung bình thấp nhất:")
        for hs in danh_sach[-10:]:
            print(f"{hs['ma_hoc_sinh']} - {hs['ho_va_ten']} - {hs['diem_tb']:.2f}")

    def them_hoc_sinh_vao_lop(danh_sach):
        lop = input("Nhập lớp muốn thêm học sinh: ")
        so_luong_hien_tai = sum(1 for hs in danh_sach if hs['lop'] == lop)

        if so_luong_hien_tai >= 40:
            print("Lớp đã đủ 40 học sinh, không thể thêm học sinh mới.")
            return

        thong_tin_moi = nhap_danh_sach_hoc_sinh()
        for hs in thong_tin_moi:
            if hs['lop'] == lop:
                danh_sach.append(hs)
                print("Thêm học sinh vào lớp thành công.")
            else:
                print(f"Học sinh {hs['ho_va_ten']} không thuộc lớp {lop}, không được thêm.")

    while True:
        print("\nMenu:")
        print("1. Hiển thị danh sách học sinh và kèm theo điểm ")
        print("2. Nhập danh sách học sinh")
        print("3. Lưu danh sách vào tệp CSV")
        print("4. Sửa điểm của học sinh")
        print("5. Đọc danh sách từ file CSV")
        print("6. Tìm kiếm học sinh theo lớp, học kỳ, năm học")
        print("7. Tìm kiếm danh sách học sinh theo lớp hoặc tên lớp")
        print("8. Xem danh sách học sinh toàn trường theo tiêu chí")
        print("9. Xếp loại học sinh theo lớp")
        print("10. Xem top 10 học sinh cao/ thấp điểm nhất")
        print("11. Thêm học sinh vào lớp mới")
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
        elif lua_chon == "6":
            tim_kiem_hoc_sinh_theo_lop_hoc_ky_nam(danh_sach_hoc_sinh)
        elif lua_chon == "7":
            tim_kiem_theo_lop_hoac_ten_lop(danh_sach_hoc_sinh)
        elif lua_chon == "8":
            xep_hoc_sinh_theo_toan_truong(danh_sach_hoc_sinh)
        elif lua_chon == "9":
            xep_loai_hoc_sinh(danh_sach_hoc_sinh)
        elif lua_chon == "10":
            top_hoc_sinh(danh_sach_hoc_sinh)
        elif lua_chon == "11":
            them_hoc_sinh_vao_lop(danh_sach_hoc_sinh)
        elif lua_chon == "0":
            print("Chương trình kết thúc.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
