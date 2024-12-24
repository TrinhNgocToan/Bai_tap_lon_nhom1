import sys

print("\n===== QUẢN LÝ HỌC SINH =====")
print("1. Quản lý lớp học")
print("2. Quản lý thông tin học sinh")
print("3. Xử lý điểm")
print("4. Thoát chương trình")
choice = float(input("Chọn chức năng (1-4): "))
if choice == 1:
    menu_quan_ly_lop_hoc()
elif choice == 2:
    menu_quan_ly_thong_tin_hoc_sinh()
elif choice == 3:
    menu_xu_ly_diem()
elif choice == 4:
    print("Kết thúc chương trình!")
    sys.exit()
else:
    print("Lựa chọn không hợp lệ. Vui lòng thử lại.")



def menu_quan_ly_lop_hoc():
    print("\n--- Quản lý lớp học ---")
    print("1. Xem lớp học")
    print("2. Thêm lớp học")
    print("3. Xóa lớp học")
    print("4. Chỉnh sửa lớp học")
    print("5. Tìm kiếm lớp học")
    print("6. Quay lại menu chính")
    choice = float(input("Chọn chức năng (1-6): "))
    if choice ==1 :
        xem_lop_hoc()
    elif choice == 2:
        them_lop_học()
    elif choice == 3:
        xoa_lop_học()
    elif choice == 4:
        chinh_sua_lop_học()
    elif choice == 5:
        tim_kiem_lop_học()
    elif choice == 6:
        menu()
    else:
        print("Bạn nhập sai yêu cầu bạn nhập lại ")
        
        
def menu_quan_ly_thong_tin_hoc_sinh():
    print("\n--- Quản lý học sinh ---")
    print("1. Xem học sinh")
    print("2. Thêm học sinh")
    print("3. Xóa học sinh")
    print("4. Chỉnh sửa thông tin học sinh")
    print("5. Tìm kiếm học sinh")
    print("6. Quay lại menu chính")
    choice = int(input("Chọn chức năng: "))

    if choice == 1:
        xem_hoc_sinh()
    elif choice == 2:
        them_hoc_sinh()
    elif choice == 3:
        xoa_hoc_sinh()
    elif choice == 4:
        chinh_sua_thong_tin_hoc_sinh()
    elif choice ==5:
        tim_kiem_hoc_sinh()
    elif choice == 6:
        menu()
    else:
        print("Bạn nhập sai yêu cầu bạn nhập lại ")
        

def menu_xu_ly_diem():
    print("\n--- Xử lý điểm học sinh ---")
    print("1. Xem học sinh kèm điểm")
    print("2. Chỉnh sửa điểm")
    print("3. Xóa điểm")
    print("4. Tìm kiếm điểm")
    print("5. Quay lại menu chính")
    if choice == 1:
        xem_hoc_sinh_kem_diem()
    elif choice == 2:
        chinh_sua_diem_cua_hoc_sinh()
    elif choice == 3:
        xoa_diem_cua_hoc_sinh()
    elif choice == 4:
        tim_kiem_diem()
    elif choice == 5:
        menu()
    else:
        print("Bạn nhập sai yêu cầu bạn nhập lại ")
        
        
