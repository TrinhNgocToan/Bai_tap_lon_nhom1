danh_sach_lop_hoc = {}

def menu_quan_ly_lop_hoc():
    while True:
        print("\n--- Quản lý lớp học ---")
        print("1. Xem lớp học")
        print("2. Thêm lớp học")
        print("3. Xóa lớp học")
        print("4. Chỉnh sửa lớp học")
        print("5. Tìm kiếm lớp học")
        print("6.Đọc và lưu file danh sách")
        print("7. Thoát")

        try:
            lua_chon = int(input("Chọn chức năng (1-7): "))
            if lua_chon == 1:
                xem_lop_hoc()
            elif lua_chon == 2:
                them_lop_hoc()
            elif lua_chon == 3:
                xoa_lop_hoc()
            elif lua_chon == 4:
                chinh_sua_lop_hoc()
            elif lua_chon == 5:
                tim_kiem_lop_hoc()
            elif lua_chon == 6:
                doc_va_luu_danh_sach()
            elif lua_chon == 7:
                print("Thoát chương trình!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        except ValueError:
            print("Vui lòng nhập số nguyên từ 1 đến 7.")

def xem_lop_hoc():
    if not danh_sach_lop_hoc:
        print("Không có lớp học nào.")
    else:
        print("\nDanh sách lớp học:")
        so_thu_tu = 1
        for ma_lop, thong_tin in danh_sach_lop_hoc.items():
            print(f"{so_thu_tu}. Mã lớp: {ma_lop}, Tên lớp: {thong_tin['Tên lớp']}, Số bàn: {thong_tin['Số bàn']}")
            so_thu_tu += 1

import csv

def them_lop_hoc():
    file_path = 'file_csv\ds_lop_hoc.csv'  # Đường dẫn tới file ds_lop_hoc.csv
    ma_lop = input("Nhập mã lớp: ")

    # Kiểm tra mã lớp đã tồn tại trong file
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Mã lớp'] == ma_lop:
                    print("Mã lớp đã tồn tại. Vui lòng nhập lại.")
                    return
    except FileNotFoundError:
        # File chưa tồn tại, sẽ được tạo khi ghi dữ liệu
        pass

    ten_lop = input("Nhập tên lớp: ")
    try:
        so_ban = int(input("Nhập số bàn: "))
        new_row = {'Mã lớp': ma_lop, 'Tên lớp': ten_lop, 'Số bàn': so_ban}

        # Ghi dữ liệu vào file (thêm tiêu đề nếu file rỗng hoặc chưa tồn tại)
        file_exists = False
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                file_exists = bool(file.read().strip())
        except FileNotFoundError:
            pass

        with open(file_path, mode='a', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Mã lớp', 'Tên lớp', 'Số bàn'])
            if not file_exists:
                writer.writeheader()  # Ghi tiêu đề nếu file chưa có nội dung
            writer.writerow(new_row)  # Ghi dòng dữ liệu mới

        print(f"Lớp học {ten_lop} đã được thêm vào file {file_path}!")
    except ValueError:
        print("Số bàn phải là một số nguyên. Vui lòng thử lại.")

import csv

def xoa_lop_hoc():
    file_path = 'file_csv\ds_lop_hoc.csv'  # Đường dẫn tới file ds_lop_hoc.csv
    ma_lop = input("Nhập mã lớp cần xóa: ")
    danh_sach_lop_hoc = []
    lop_ton_tai = False

    # Đọc dữ liệu từ file
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Mã lớp'] == ma_lop:
                    lop_ton_tai = True  # Đánh dấu lớp cần xóa
                else:
                    danh_sach_lop_hoc.append(row)  # Giữ lại các lớp khác
    except FileNotFoundError:
        print("File không tồn tại. Không thể xóa lớp học.")
        return

    # Nếu lớp học tồn tại, ghi lại danh sách mới vào file
    if lop_ton_tai:
        with open(file_path, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['Mã lớp', 'Tên lớp', 'Số bàn']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Ghi tiêu đề
            writer.writerows(danh_sach_lop_hoc)  # Ghi các lớp còn lại
        print(f"Lớp học với mã {ma_lop} đã được xóa!")
    else:
        print(f"Lớp học với mã {ma_lop} không tồn tại!")


def chinh_sua_lop_hoc():
    try:
        with open("package_quan_ly_lop_hoc/file_ds_lop_hoc.csv", mode="r") as file:
            lines = file.readlines()
            if not lines:
                print("Danh sách lớp học hiện tại trống.")
                return
            print("Danh sách lớp học:")
            so_thu_tu = 1
            for line in lines:
                print(f"{so_thu_tu}. {line.strip()}")
                so_thu_tu += 1

            lop_stt = int(input("Chọn lớp học để chỉnh sửa (số thứ tự): "))
            if lop_stt < 1 or lop_stt > len(lines):
                print("Lựa chọn không hợp lệ.")
                return

            chinh_sua_lop = lines[lop_stt - 1].strip()
            print(f"Chỉnh sửa lớp: {chinh_sua_lop}")
            lop_moi = input("Nhập tên lớp học mới: ")

            lines[lop_stt - 1] = lop_moi + "\n"
            with open("package_quan_ly_lop_hoc/file_ds_lop_hoc.csv", mode="w") as file:
                file.writelines(lines)

            print("Lớp học đã được chỉnh sửa thành công.")
    except (FileNotFoundError, ValueError):
        print("Tệp danh sách lớp học không tìm thấy hoặc lỗi nhập liệu!")

def tim_kiem_lop_hoc():
    tu_khoa = input("Nhập tên lớp học để tìm kiếm: ").strip()
    try:
        with open("package_quan_ly_lop_hoc/file_ds_lop_hoc.csv", mode="r") as file:
            lines = file.readlines()
            ket_qua = []
            so_thu_tu = 1
            for line in lines:
                if tu_khoa.lower() in line.lower():
                    ket_qua.append(f"{so_thu_tu}. {line.strip()}")
                    so_thu_tu += 1

            if ket_qua:
                print("Lớp học tìm thấy:")
                for lop in ket_qua:
                    print(lop)
            else:
                print("Không tìm thấy lớp học khớp với yêu cầu.")
    except FileNotFoundError:
        print("Tệp danh sách lớp học không tìm thấy.")

import csv

def doc_va_luu_danh_sach(danh_sach_lop_hoc):
    while True:
        print("\n--- Quản lý danh sách lớp học ---")
        print("1. Đọc danh sách từ file")
        print("2. Lưu danh sách vào file")
        print("3. Thoát")

        try:
            lua_chon = int(input("Chọn chức năng (1-3): "))
            if lua_chon == 1:
                try:
                    with open(file="file_csv/ds_lop_hoc.csv", mode="r") as open_file:
                        csv_reader = csv.reader(open_file)
                        danh_sach_lop_hoc = {row[0]: {'Tên lớp': row[1], 'Số bàn': int(row[2])} for row in csv_reader}
                        print("Đã đọc danh sách từ file:")
                        xem_lop_hoc(danh_sach_lop_hoc)
                except FileNotFoundError:
                    print("Không tìm thấy file để đọc danh sách.")
            elif lua_chon == 2:
                try:
                    with open(file="file_csv/ds_lop_hoc.csv", mode="w", newline='') as open_file:
                        csv_writer = csv.writer(open_file)
                        for ma_lop, thong_tin in danh_sach_lop_hoc.items():
                            csv_writer.writerow([ma_lop, thong_tin['Tên lớp'], thong_tin['Số bàn']])
                        print("Danh sách đã được lưu vào file.")
                except Exception as e:
                    print(f"Lỗi khi lưu danh sách vào file: {e}")
            elif lua_chon == 3:
                print("Thoát quản lý danh sách lớp học.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
        except ValueError:
            print("Vui lòng nhập số nguyên từ 1 đến 3.")

    return danh_sach_lop_hoc

