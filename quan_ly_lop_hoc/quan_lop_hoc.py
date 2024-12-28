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

import csv

def xem_lop_hoc():
    file_path = 'file_csv\ds_lop_hoc.csv' 
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            danh_sach_lop_hoc = list(reader)

        if not danh_sach_lop_hoc:
            print("Không có lớp học nào.")
            return

        sap_xep = input("Bạn muốn sắp xếp theo mã lớp (nhập 'M') hay tên lớp (nhập 'T'): ").strip().upper()
        if sap_xep == 'M':
            danh_sach_lop_hoc.sort(key=lambda x: x['Mã lớp'])
        elif sap_xep == 'T':
            danh_sach_lop_hoc.sort(key=lambda x: x['Tên lớp'])
        else:
            print("Lựa chọn không hợp lệ. Hiển thị danh sách không sắp xếp.")

        print("\nDanh sách lớp học:")
        for so_thu_tu, lop in enumerate(danh_sach_lop_hoc, start=1):
            print(f"{so_thu_tu}. Mã lớp: {lop['Mã lớp']}, Tên lớp: {lop['Tên lớp']}, Số bàn: {lop['Số bàn']}")

    except FileNotFoundError:
        print("Tệp ds_lop_hoc.csv không tồn tại!")
    except :
        print("Tệp ds_lop_hoc.csv không đúng định dạng yêu cầu!")

import csv

import csv

def them_lop_hoc():
    file_path = 'file_csv\ds_lop_hoc.csv'  
    ma_lop = input("Nhập mã lớp (tối đa 10 ký tự): ")

    if len(ma_lop) > 10:
        print("Mã lớp không được vượt quá 10 ký tự. Vui lòng nhập lại.")
        return

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Mã lớp'] == ma_lop:
                    print("Mã lớp đã tồn tại. Vui lòng nhập lại.")
                    return
    except :
        pass

    ten_lop = input("Nhập tên lớp (tối đa 20 ký tự): ")

    if len(ten_lop) > 20:
        print("Tên lớp không được vượt quá 20 ký tự. Vui lòng nhập lại.")
        return

    try:
        so_ban = int(input("Nhập số bàn (tối đa 40 bàn): "))

        if so_ban <= 0 or so_ban > 40:
            print("Số bàn phải là một số nguyên dương và không vượt quá 40. Vui lòng nhập lại.")
            return

        new_row = {'Mã lớp': ma_lop, 'Tên lớp': ten_lop, 'Số bàn': so_ban}

        
        file_exists = False
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                file_exists = bool(file.read().strip())
        except FileNotFoundError:
            pass

        with open(file_path, mode='a', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Mã lớp', 'Tên lớp', 'Số bàn'])
            if not file_exists:
                writer.writeheader() 
            writer.writerow(new_row) 

        print(f"Lớp học {ten_lop} đã được thêm vào file {file_path}!")
    except ValueError:
        print("Số bàn phải là một số nguyên. Vui lòng thử lại.")

import csv

def xoa_lop_hoc():
    file_path = 'file_csv\ds_lop_hoc.csv' 
    ma_lop = input("Nhập mã lớp cần xóa: ")
    danh_sach_lop_hoc = []
    lop_ton_tai = False

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Mã lớp'] == ma_lop:
                    lop_ton_tai = True  
                else:
                    danh_sach_lop_hoc.append(row)  
    except FileNotFoundError:
        print("File không tồn tại. Không thể xóa lớp học.")
        return

   
    if lop_ton_tai:
        with open(file_path, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['Mã lớp', 'Tên lớp', 'Số bàn']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader() 
            writer.writerows(danh_sach_lop_hoc) 
        print(f"Lớp học với mã {ma_lop} đã được xóa!")
    else:
        print(f"Lớp học với mã {ma_lop} không tồn tại!")




import csv

def chinh_sua_lop_hoc():
    file_path = 'file_csv\ds_lop_hoc.csv'  

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            danh_sach_lop_hoc = list(reader)

        if not danh_sach_lop_hoc:
            print("Danh sách lớp học hiện tại trống.")
            return

        print("Danh sách lớp học:")
        for i, lop in enumerate(danh_sach_lop_hoc, start=1):
            print(f"{i}. Mã lớp: {lop['Mã lớp']}, Tên lớp: {lop['Tên lớp']}, Số bàn: {lop['Số bàn']}")

        ma_or_ten = input("Bạn muốn chỉnh sửa theo mã lớp (nhập 'M') hay tên lớp (nhập 'T'): ").strip().upper()
        if ma_or_ten == 'M':
            ma_lop = input("Nhập mã lớp để chỉnh sửa: ").strip()
            lop_cu = next((lop for lop in danh_sach_lop_hoc if lop['Mã lớp'] == ma_lop), None)
        elif ma_or_ten == 'T':
            ten_lop = input("Nhập tên lớp để chỉnh sửa: ").strip()
            lop_cu = next((lop for lop in danh_sach_lop_hoc if lop['Tên lớp'] == ten_lop), None)
        else:
            print("Lựa chọn không hợp lệ.")
            return

        if not lop_cu:
            print("Lớp học không tồn tại.")
            return

        print(f"Chỉnh sửa lớp: Mã lớp: {lop_cu['Mã lớp']}, Tên lớp: {lop_cu['Tên lớp']}, Số bàn: {lop_cu['Số bàn']}")

        ten_lop_moi = input("Nhập tên lớp học mới: ").strip()
        so_ban_moi = input("Nhập số bàn mới: ").strip()

        if not so_ban_moi.isdigit():
            print("Số bàn phải là một số nguyên. Vui lòng thử lại.")
            return

        lop_cu['Tên lớp'] = ten_lop_moi
        lop_cu['Số bàn'] = so_ban_moi

        with open(file_path, mode="w", encoding="utf-8", newline='') as file:
            fieldnames = ['Mã lớp', 'Tên lớp', 'Số bàn']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(danh_sach_lop_hoc)

        print("Lớp học đã được chỉnh sửa thành công.")
    except FileNotFoundError:
        print("Tệp ds_lop_hoc.csv không tồn tại!")
    except ValueError:
        print("Lỗi nhập liệu! Vui lòng nhập một giá trị hợp lệ.")

import csv

def tim_kiem_lop_hoc():
    file_path = 'file_csv/ds_lop_hoc.csv' 

    try:
        tu_khoa = input("Nhập mã lớp hoặc tên lớp học để tìm kiếm: ").strip()

        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            danh_sach_lop_hoc = list(reader)

        ket_qua = [lop for lop in danh_sach_lop_hoc if tu_khoa.lower() in lop['Mã lớp'].lower() or tu_khoa.lower() in lop['Tên lớp'].lower()]

        if ket_qua:
            print("Lớp học tìm thấy:")
            for lop in ket_qua:
                print(f"Mã lớp: {lop['Mã lớp']}, Tên lớp: {lop['Tên lớp']}, Số bàn: {lop['Số bàn']}")
                if 'Danh sách học sinh' in lop and lop['Danh sách học sinh'].strip():
                    print(f"Danh sách học sinh: {lop['Danh sách học sinh']}")
                else:
                    print("Danh sách học sinh: Không có thông tin.")
        else:
            print("Không tìm thấy lớp học khớp với yêu cầu.")

    except FileNotFoundError:
        print("Tệp ds_lop_hoc.csv không tồn tại!")
    except KeyError:
        print("Tệp ds_lop_hoc.csv không đúng định dạng yêu cầu!")

import csv
import os

def doc_va_luu_danh_sach():
    file_path = 'file_csv/ds_lop_hoc.csv'  
    danh_sach_lop_hoc = {}

    if os.path.exists(file_path):
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    danh_sach_lop_hoc[row['Mã lớp']] = {
                        'Tên lớp': row['Tên lớp'],
                        'Số bàn': int(row['Số bàn']),
                        'Danh sách học sinh': row['Danh sách học sinh'] if 'Danh sách học sinh' in row else ''
                    }
            print("Dữ liệu đã được đọc từ file ds_lop_hoc.csv:")
            for ma_lop, thong_tin in danh_sach_lop_hoc.items():
                print(f"Mã lớp: {ma_lop}, Tên lớp: {thong_tin['Tên lớp']}, Số bàn: {thong_tin['Số bàn']}, Danh sách học sinh: {thong_tin['Danh sách học sinh']}")
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")
    else:
        print("File ds_lop_hoc.csv không tồn tại. Bắt đầu với danh sách trống.")

    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['Mã lớp', 'Tên lớp', 'Số bàn', 'Danh sách học sinh']
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

            csv_writer.writeheader()
            for ma_lop, thong_tin in danh_sach_lop_hoc.items():
                csv_writer.writerow({
                    'Mã lớp': ma_lop,
                    'Tên lớp': thong_tin['Tên lớp'],
                    'Số bàn': thong_tin['Số bàn'],
                    'Danh sách học sinh': thong_tin['Danh sách học sinh']
                })
            print("Dữ liệu đã được lưu vào file ds_lop_hoc.csv.")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

