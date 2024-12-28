from datetime import datetime
ds_hoc_sinh = []
n = int(input("Nhap so sinh vien n = "))
def xem_hoc_sinh_kem_diem(n):
    
    for sinh_vien in range(n):
        print(f"Nhap thong tin sinh vien thu {sinh_vien + 1}:")
        ma_sinh_vien=float(input("Nhap ma sinh vien: "))
        ho_dem= input(" Nhâp họ và tên đệm: ")
        ten = input("Nhap ten sinh vien: ")
        tuoi=int(input("Nhập số tuổi của học sinh"))
        ngay_sinh_str = input("Nhập ngày tháng năm sinh (dd/mm/yyyy): ").strip()
        ngay_sinh = datetime.strptime(ngay_sinh_str, '%d/%m/%Y')
        so_dien_thoai=str(input("Nhập số điện thoại: "))
        ma_lop=str(input("Nhập mã lớp: "))
        diem_toan = float(input("Nhap diem toan sinh vien: "))
        diem_ly= float(input("Nhap diem ly sinh vien: "))
        diem_hoa= float(input("Nhap diem hoa sinh vien: "))
        diem_anh= float(input("Nhap diem anh sinh vien: "))
        diem_van= float(input("Nhap diem van sinh vien: "))
        diem_trung_binh=(diem_toan+diem_hoa+diem_ly)/5
        hoc_ki=str(input("Học kì: "))
        nam_hoc=str(input("Năm học: "))
        ma_hoc_ki=str(input("Nhập mã học kì: "))
        thong_tin_hoc_sinh = {"ma sinh vien":ma_sinh_vien,"ho dem":ho_dem,"ten": ten,"tuoi": tuoi,"ngay thang nam sinh":ngay_sinh,"so dien thoai":so_dien_thoai,"ma lop":ma_lop,"diem toan":diem_toan, "diem ly":diem_ly,"diem hoa":diem_hoa,"diem anh":diem_anh,"diem van":diem_van,"diem trung binh":diem_trung_binh,"hoc ki":hoc_ki,"nam hoc":nam_hoc,"ma hoc ki":ma_hoc_ki}
        ds_hoc_sinh.append(thong_tin_hoc_sinh)
    print("Mã học sinh    Họ đệm    Tên    Tuổi    Ngày/tháng/năm sinh    Số điện thoại    Mã lớp    Điểm toán    Điểm hoá    Điểm lý    Điểm anh    Điểm văn    Điểm trung bình    Học kì    Năm học    Mã học kì")
    for hoc_sinh in ds_hoc_sinh:
        print(f"{hoc_sinh['ma sinh vien']}    {hoc_sinh['ho dem']}    {hoc_sinh['ten']}    {hoc_sinh['tuoi']}    {hoc_sinh['ngay thang nam sinh']}    {hoc_sinh['so dien thoai']}    {hoc_sinh['ma lop']}     {hoc_sinh['diem toan']:.1f}     {hoc_sinh['diem ly']:.1f}     {hoc_sinh['diem hoa']:.1f}    {hoc_sinh['diem anh']:.1f}    {hoc_sinh['diem van']:.1f}     {hoc_sinh['diem trung binh']:.1f}    {hoc_sinh['hoc ki']}    {hoc_sinh['nam hoc']}    {hoc_sinh['ma hoc ki']}")
xem_hoc_sinh_kem_diem(n)       