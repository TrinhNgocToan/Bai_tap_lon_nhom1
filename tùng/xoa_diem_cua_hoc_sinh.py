def xoa_diem_cua_hoc_sinh(ds_hoc_sinh):
    ten_can_xoa = input("Nhập tên sinh viên cần xóa: ")
    for sinh_vien in ds_hoc_sinh:
        if sinh_vien["ten"] == ten_can_xoa:
            print("Menu")
            print("1,Xoá điểm toán")
            print("2,Xoá điểm hoá")
            print("3,Xoá điểm lý")
            print("4,Xoá điểm anh")
            print("Xoá điểm văn")
            choice=None
            while True:
                choice=input("Nhấp lựa chọn của bạn (0 để thoát)")
                if kiem_tra_choice(choice)==True:
                    if choice=='1':
                        ds_hoc_sinh['diem toan'].remove(sinh_vien)
                        print(f"Đã xóa điểm toán của sinh viên {ten_can_xoa} khỏi danh sách.")
                        break
                    elif choice=='2':   
                        ds_hoc_sinh['diem hoa'].remove(sinh_vien)
                        print(f"Đã xóa điểm hoá của sinh viên {ten_can_xoa} khỏi danh sách.")
                        break
                    elif choice=='3':
                        ds_hoc_sinh['diem_ly'].remove(sinh_vien)
                        print(f"Đã xóa điểm lý của sinh viên {ten_can_xoa} khỏi danh sách.")
                        break
                    elif choice=='4':
                        ds_hoc_sinh['diem_anh'].remove(sinh_vien)
                        print(f"Đã xóa điểm anh của sinh viên {ten_can_xoa} khỏi danh sách.")
                        break
                    elif choice=='5':
                        ds_hoc_sinh['diem_van'].remove(sinh_vien)
                        print(f"Đã xóa điểm văn của sinh viên {ten_can_xoa} khỏi danh sách.")
                        break
                    elif choice=='0':
                        print("Kết thúc chương trình")
                    else:
                        print("Hãy nhập từ 0 đến 5") 
                else:
                    print("Hãy nhập số nguyên")   
                
        else:
               print(f"Không tìm thấy sinh viên có tên {ten_can_xoa}.")
    print("Danh sách sinh viên sau khi xóa:")
    for sinh_vien in ds_hoc_sinh:
            print(f"{sinh_vien['ten']}   {sinh_vien['diem toan']}   {sinh_vien['diem hoa']}   {sinh_vien['diem ly']}   {sinh_vien['diem anh']}   {sinh_vien['van']}")
            
def kiem_tra_choice(choice):
        if choice.isdigit()==True:
                return True
        else:
                return False