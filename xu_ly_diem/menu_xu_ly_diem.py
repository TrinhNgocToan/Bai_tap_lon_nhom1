import csv
from datetime import datetime
def menu_xu_ly_diem_hoc_sinh():
    danh_sach_hoc_sinh = []

    def nhap_danh_sach_hoc_sinh():
        danh_sach = []
        so_luong = int(input("Nhập số lượng học sinh: "))

        for i in range(so_luong):
            print(f"Nhập thông tin cho học sinh thứ {i + 1}:")
            while True:
                ma_hoc_sinh = input("Mã học sinh (10 ký tự): ")
                if len(ma_hoc_sinh) <= 10:
                    break
                else:
                    print("Mã học sinh phải có đúng 10 ký tự.")
            while True:
                ho_va_ten = input("Họ và tên (tối đa 50 ký tự): ")
                if len(ho_va_ten) <= 50:
                    break
                else:
                    print("Họ và tên không được vượt quá 50 ký tự.")
            while True:
                try:
                    tuoi = int(input("Tuổi: "))
                    if tuoi > 0:
                        break
                    else:
                        print("Tuổi phải là một số dương.")
                except ValueError:
                    print("Vui lòng nhập tuổi là một số nguyên hợp lệ.")
            while True:
                try:
                    ngay_sinh = input("Ngày sinh (dd/mm/yyyy): ")
                    ngay_sinh = datetime.strptime(ngay_sinh, '%d/%m/%Y')
                    break
                except ValueError:
                    print("Ngày sinh không hợp lệ, vui lòng nhập lại theo định dạng dd/mm/yyyy.")
            while True:
                so_dien_thoai = input("Số điện thoại (10 ký tự): ")
                if len(so_dien_thoai) == 10 and so_dien_thoai.isdigit():
                    break
                else:
                    print("Số điện thoại phải có 10 ký tự và là số.")
            while True:
                lop = input("Mã lớp (10 ký tự): ")
                if len(lop) <= 10:
                    break
                else:
                    print("Mã lớp phải có đúng 10 ký tự.")
            while True:
                try:
                    diem_toan = float(input("Điểm Toán (0 <= điểm <= 10): "))
                    if 0 <= diem_toan <= 10:
                        break
                    else:
                        print("Điểm phải nằm trong khoảng từ 0 đến 10.")
                except ValueError:
                    print("Vui lòng nhập điểm là một số hợp lệ.")
            
            while True:
                try:
                    diem_ly = float(input("Điểm Lý (0 <= điểm <= 10): "))
                    if 0 <= diem_ly <= 10:
                        break
                    else:
                        print("Điểm phải nằm trong khoảng từ 0 đến 10.")
                except ValueError:
                    print("Vui lòng nhập điểm là một số hợp lệ.")
            while True:
                try:
                    diem_hoa = float(input("Điểm Hóa (0 <= điểm <= 10): "))
                    if 0 <= diem_hoa <= 10:
                        break
                    else:
                        print("Điểm phải nằm trong khoảng từ 0 đến 10.")
                except ValueError:
                    print("Vui lòng nhập điểm là một số hợp lệ.")
            while True:
                try:
                    diem_anh = float(input("Điểm Anh (0 <= điểm <= 10): "))
                    if 0 <= diem_anh <= 10:
                        break
                    else:
                        print("Điểm phải nằm trong khoảng từ 0 đến 10.")
                except ValueError:
                    print("Vui lòng nhập điểm là một số hợp lệ.")
            while True:
                try:
                    diem_van = float(input("Điểm Văn (0 <= điểm <= 10): "))
                    if 0 <= diem_van <= 10:
                        break
                    else:
                        print("Điểm phải nằm trong khoảng từ 0 đến 10.")
                except ValueError:
                    print("Vui lòng nhập điểm là một số hợp lệ.")
            diem_tb = (diem_toan + diem_ly + diem_hoa + diem_anh + diem_van) / 5
            while True:
                hoc_ky = input("Học kỳ (tối đa 10 ký tự): ")
                if len(hoc_ky) <= 10:
                    break
                else:
                    print("Học kỳ không được vượt quá 10 ký tự.")
            while True:
                nam_hoc = input("Năm học (4 ký tự): ")
                if len(nam_hoc) == 4 and nam_hoc.isdigit():
                    break
                else:
                    print("Năm học phải có 4 ký tự và là số.")
            while True:
                ma_hoc_ky = input("Mã học kỳ (10 ký tự): ")
                if len(ma_hoc_ky) <= 10:
                    break
                else:
                    print("Mã học kỳ phải có đúng 10 ký tự.")
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
                "diem_anh": diem_anh,
                "diem_van": diem_van,
                "diem_tb": diem_tb,
                "hoc_ky": hoc_ky,
                "nam_hoc": nam_hoc,
                "ma_hoc_ky": ma_hoc_ky
            }
            danh_sach.append(thong_tin_hoc_sinh)

        return danh_sach
    danh_sach_hoc_sinh = nhap_danh_sach_hoc_sinh()

    def hien_thi_danh_sach_hoc_sinh(danh_sach):
        if not danh_sach:
            print("Danh sách học sinh trống.")
            return
        print("Mã HS | Họ và tên       | Tuổi | Ngày sinh | SĐT       | Lớp | Toán | Lý | Hóa | Anh | Văn | Điểm TB | Học kỳ | Năm học | Mã học kỳ")
        print("-" * 100)
        for hs in danh_sach:
            print(f"{hs['ma_hoc_sinh']} | {hs['ho_va_ten']:<15} | {hs['tuoi']}   | {hs['ngay_sinh']} | {hs['so_dien_thoai']:<10} | {hs['lop']} | {hs['diem_toan']:.1f} | {hs['diem_ly']:.1f} | {hs['diem_hoa']:.1f} | {hs['diem_anh']:.1f} | {hs['diem_van']:.1f} | {hs['diem_tb']:.2f} | {hs['hoc_ky']} | {hs['nam_hoc']} | {hs['ma_hoc_ky']}")
    def luu_file_csv(danh_sach):
        if not danh_sach:
            print("Danh sách trống, không có gì để lưu.")
            return
        with open("file_csv/ds_diem.csv", mode="w", newline="") as open_file:
            csv_writer = csv.writer(open_file)
            csv_writer.writerow(danh_sach) 
            for hs in danh_sach:
                csv_writer.writerow(hs)
        print("Lưu danh sách học sinh thành công.")
    def doc_file_csv(danh_sach: list):
        with open("file_csv/ds_diem.csv", mode="r", newline="") as open_file:
            csv_reader = csv.reader(open_file)
            for hs in csv_reader:
                print(hs)
                danh_sach.append(hs)
        print("Lưu danh sách học sinh thành công.")



    def sua_diem_hoc_sinh(danh_sach):
        ma_hoc_sinh = input("Nhập mã học sinh cần sửa điểm: ")
        for hs in danh_sach:
            if hs['ma_hoc_sinh'] == ma_hoc_sinh:
                print(f"Sửa điểm cho học sinh {hs['ho_va_ten']}:")
                hs['diem_toan'] = float(input("Nhập điểm Toán mới: "))
                hs['diem_ly'] = float(input("Nhập điểm Lý mới: "))
                hs['diem_hoa'] = float(input("Nhập điểm Hóa mới: "))
                hs['diem_anh'] = float(input("Nhập điểm Anh mới: "))
                hs['diem_van'] = float(input("Nhập điểm Văn mới: "))
                hs['diem_tb'] = (hs['diem_toan'] + hs['diem_ly'] + hs['diem_hoa'] + hs['diem_anh'] + hs['diem_van']) / 5
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
            danh_sach.append(hien_thi_danh_sach_hoc_sinh)

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
        print("8. Xem danh sách học sinh toàn trường được sắp xếp theo điểm trung bình hoặc mã học sinh ")
        print("9. Xếp loại học sinh theo lớp")
        print("10. Xem top 10 học sinh cao/ thấp điểm nhất")
        print("11. Thêm học sinh vào lớp mới")
        print("0. Thoát")
        lua_chon = input("Nhập lựa chọn: ")
        if lua_chon == "1":
            hien_thi_danh_sach_hoc_sinh(danh_sach_hoc_sinh)
        elif lua_chon == "2":
            danh_sach_hoc_sinh = nhap_danh_sach_hoc_sinh()
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
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")

