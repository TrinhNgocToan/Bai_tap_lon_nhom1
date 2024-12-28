def chinh_sua_diem_cua_hoc_sinh(ds_hoc_sinh):
    ten_can_sua = input("Nhập tên sinh viên cần sửa thông tin: ")
    tim_ten = False
    for hoc_sinh in ds_hoc_sinh:
        if hoc_sinh['ten'] == ten_can_sua:
                tim_ten = True
                choice=None
                print("Menu")
                print("1.Chỉnh sửa điểm toán")
                print("2.Chỉnh sửa điểm hoá")
                print("3,Chỉnh sửa điểm lý")
                print("4,Chỉnh sửa điểm anh")
                print("5,Chỉnh sửa điểm văn")
                while choice==0:
                        choice=input(f"Nhập lưa chọn của bạn(0 để thoát): ")
                        if kiem_tra_choice(choice):
                                if choice==1:
                                        diem_toan_moi = float(input(f"Nhập điểm mới cho sinh viên {ten_can_sua}: "))
                                        hoc_sinh['diem toan'] = diem_toan_moi
                                        print(f"Đã sửa điểm của sinh viên {ten_can_sua} thành {diem_toan_moi}.")
                                elif choice==2:
                                        diem_hoa_moi = float(input(f"Nhập điểm mới cho sinh viên {ten_can_sua}: "))
                                        hoc_sinh['diem hoa'] = diem_hoa_moi
                                        print(f"Đã sửa điểm của sinh viên {ten_can_sua} thành {diem_hoa_moi}.")
                                elif choice==3:
                                        diem_ly_moi = float(input(f"Nhập điểm mới cho sinh viên {ten_can_sua}: "))
                                        hoc_sinh['diem ly'] = diem_ly_moi
                                        print(f"Đã sửa điểm của sinh viên {ten_can_sua} thành {diem_ly_moi}.")
                                elif choice==4:
                                        diem_anh_moi = float(input(f"Nhập điểm mới cho sinh viên {ten_can_sua}: "))
                                        hoc_sinh['diem anh'] = diem_anh_moi
                                        print(f"Đã sửa điểm của sinh viên {ten_can_sua} thành {diem_anh_moi}.")
                                        break
                                elif choice==5:
                                        diem_van_moi = float(input(f"Nhập điểm mới cho sinh viên {ten_can_sua}: "))
                                        hoc_sinh['diem van'] = diem_van_moi
                                        print(f"Đã sửa điểm của sinh viên {ten_can_sua} thành {diem_van_moi}.")
                                        break
                                elif choice==0:
                                        print("Kết thúc chương trình")
                                else:
                                        print("Nhập số từ 0 đến 5")
                        else:
                                print("Xin hãy nhập số nguyên")                                       
        if not tim_ten:
            print(f"Không tìm thấy sinh viên có tên {ten_can_sua}.")
        print("Danh sách sinh viên sau khi sửa:")
    for sinh_vien in ds_hoc_sinh:
            print(f"{sinh_vien['ten']}   {sinh_vien['diem toan']}   {sinh_vien['diem hoa']}   {sinh_vien['diem ly']}   {sinh_vien['diem anh']}   {sinh_vien['van']}")
            
def kiem_tra_choice(choice):
        if choice.isdigit()==True:
                return True
        else:
                return False