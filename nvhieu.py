
def chinh_sua_lop_hoc():
    try:
        with open("package_quan_ly_lop_hoc/file_ds_lop_hoc.csv", mode="r") as file:
            lines = file.readlines()
            if not lines:
                print("Danh sách lớp học hiện tại trống.")
                return
            print("Danh sách lớp học:")
            for idx, line in enumerate(lines, start=1):
                print(f"{idx}. {line.strip()}")

            try:
                lop_stt = int(input("Chọn lớp học để chỉnh sửa (số thứ tự): "))
                if lop_stt < 1 or lop_stt > len(lines):
                    print("Lựa chọn không hợp lệ.")
                    return
            except ValueError:
                print("Lựa chọn không hợp lệ.NHập lại")
                return

            
            chinh_sua_lop = lines[lop_stt - 1].strip() #Hiện thông tin lớp học cũ và nhận thông tin mới 
            print(f"Chỉnh sửa lớp: {chinh_sua_lop}")
            lop_moi = input("Nhập tên lớp học mới: ")

        
            lines[lop_stt - 1] = lop_moi + "\n" #Cập nhập lớp trong danh sách

            
            with open("package_quan_ly_lop_hoc/file_ds_lop_hoc.csv", mode="w") as file: #Lưu phần đã cập nhật 
                file.writelines(lines)

            print("Lớp học đã được chỉnh sửa thành công.")
    except:    #trừ khi tệp ko tìm thâý lỗi 
        print("Tệp danh sách lớp học không tìm thấy! VUI LÒNG NHẬP LẠI")



def tim_kiem_lop_hoc():
    tim_kiem = input("Nhập tên lớp học để tìm kiếm: ").strip()
    
    try:
        with open("package_quan_ly_lop_hoc/file_ds_lop_hoc.csv", mode="r") as file:
            lines = file.readlines()
            lop_khac = [line.strip() for line in lines if tim_kiem.lower() in line.lower()]

            if lop_khac:
                print("Lớp học tìm thấy:")
                for stt, ten_lop_moi in enumerate(lop_khac, start=1):
                    print(f"{stt}. {ten_lop_moi}")
            else:
                print("Không tìm thấy lớp học khớp với yêu cầu.")
    except:
        print("Tệp danh sách lớp học không tìm thấy.")




