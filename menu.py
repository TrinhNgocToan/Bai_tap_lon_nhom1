import sys
import quan_ly_lop_hoc.quan_lop_hoc as p 
import quan_ly_thong_tin_sinh.quan_ly_thong_tin_hoc_sinh as c 
import xu_ly_diem.menu_xu_ly_diem as v 
print("\n===== QUẢN LÝ HỌC SINH =====")
print("1. Quản lý lớp học")
print("2. Quản lý thông tin học sinh")
print("3. Xử lý điểm")
print("4. Thoát chương trình")
choice = float(input("Chọn chức năng (1-4): "))
if choice == 1:
    p.menu_quan_ly_lop_hoc()
elif choice == 2:
    c.quan_ly_thong_tin_hoc_sinh()
elif choice == 3:
    v.menu_xu_ly_diem_hoc_sinh()
elif choice == 4:
    print("Kết thúc chương trình!")
    sys.exit()
else:
    print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
